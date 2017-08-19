Eclipse Test & Performance Tools Platform Project troubles
##########################################################
:date: 2008-03-18 11:58
:author: infram
:category: Misc
:tags: BachelorArbeit, debug, java, java debugging interface, jdi, jvm, Programming, single step event
:slug: eclipse-test-performance-tools-platform-project-troubles
:status: published

After using TPTP for about a half year for my bachelor I am at a point
where I would remove it. But I don't have to decide it. I reported so
far `6
bugs <https://bugs.eclipse.org/bugs/buglist.cgi?bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&email1=mascha%40ma-scha.de&emailtype1=exact&emailassigned_to1=1&emailreporter1=1>`__.
Everyone of them detains me on profiling. I can create single traces but
if I repeat tracing I am in trouble. JVM crashes, 100% CPU usages and so
on. I have now written my own "profiler" two classes that give me the
covered lines back of a profiled program. It uses the Java debugging
interface (JDI).

The first class is called Agent that starts a event catcher thread (the
debugging agent) if it is called without any arguments. This debugging
agent waits for a connecting JVM. With a argument it calls a sample
method to test profiling. You have to supply the debugging agent port
and host like
*-agentlib:jdwp=transport=dt\_socket,suspend=y,address=localhost:55555*.
The other class is EventCatcherThread which enables the single step
event and waits for a connecting JVM to profile a program. Only 278
lines of java code are necessary.

**Agent.java**

::

    import java.util.ArrayList;
    import java.util.Iterator;
    import java.util.List;

    import com.sun.jdi.connect.IllegalConnectorArgumentsException;
    import com.sun.jdi.connect.VMStartException;

    public class Agent {

        private ArrayList<String> _linesPassed = new ArrayList<String>();

        public void addSourceCodeLine() {
            _linesPassed.add("bla");
        }

        public List<String> getLinesPassed() {
            return _linesPassed;
        }

        public static void debug() throws Exception {
            List<String> passedLine = new ArrayList<String>();
            EventCatcherThread eventThread = EventCatcherThread.connectToVm(55555);
            eventThread.setPassedCodeLines(passedLine);
            eventThread.start();
            eventThread.resumeVM();
            eventThread.join();

            for (Iterator<String> iterator = passedLine.iterator(); iterator
                    .hasNext();) {
                String lineKey = (String) iterator.next();
                System.out.println(lineKey);
            }
        }

        public static void main(String[] args) throws Exception,
                IllegalConnectorArgumentsException, VMStartException {
            if (args.length != 0) {
                debug();
            } else {
                Agent agent = new Agent();
                agent.traceTest();
            }
        }

        public void traceTest() {
            String string = new String();
            string = string + " fdgvdf ";
            string = string.concat("bla");
            System.out.println(string);
        }
    }

**EventCatcherThread.java**

::

    package org.projectory.ezunit;

    import java.io.IOException;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;

    import org.eclipse.jdi.Bootstrap;

    import com.sun.jdi.AbsentInformationException;
    import com.sun.jdi.ThreadReference;
    import com.sun.jdi.VMDisconnectedException;
    import com.sun.jdi.VirtualMachine;
    import com.sun.jdi.connect.AttachingConnector;
    import com.sun.jdi.connect.IllegalConnectorArgumentsException;
    import com.sun.jdi.connect.Connector.Argument;
    import com.sun.jdi.event.Event;
    import com.sun.jdi.event.EventIterator;
    import com.sun.jdi.event.EventQueue;
    import com.sun.jdi.event.EventSet;
    import com.sun.jdi.event.StepEvent;
    import com.sun.jdi.event.VMDeathEvent;
    import com.sun.jdi.event.VMDisconnectEvent;
    import com.sun.jdi.event.VMStartEvent;
    import com.sun.jdi.request.EventRequest;
    import com.sun.jdi.request.EventRequestManager;
    import com.sun.jdi.request.StepRequest;

    public class EventCatcherThread extends Thread {

        private final VirtualMachine _vm;

        private String[] _excludes;

        private boolean _connected = true;

        private String[] _includes;

        private Map<String, Location> _lineStat = new HashMap<String, Location>();

        private List<String> _passedCodeLines;

        EventCatcherThread(VirtualMachine vm, String[] excludes, String[] includes) {
            super("event-handler");
            _vm = vm;
            _excludes = excludes;
            _includes = includes;
        }

        public void run() {
            EventQueue queue = _vm.eventQueue();
            List<ThreadReference> allThreads = _vm.allThreads();
            for (ThreadReference thread : allThreads) {
                if (thread.uniqueID() == 1) {
                    enableSingleStepEvent(thread);
                }
            }

            while (_connected) {
                try {
                    EventSet eventSet = queue.remove();
                    EventIterator it = eventSet.eventIterator();
                    while (it.hasNext()) {
                        Event nextEvent = it.nextEvent();
                        handleEvent(nextEvent);
                    }
                    eventSet.resume();
                } catch (InterruptedException exc) {
                    // Ignore
                } catch (VMDisconnectedException discExc) {
                    handleDisconnectedException();
                    break;
                }
            }
        }

        private void enableSingleStepEvent(ThreadReference thread) {
            EventRequestManager mgr = _vm.eventRequestManager();
            StepRequest req = mgr.createStepRequest(thread, StepRequest.STEP_LINE,
                    StepRequest.STEP_INTO);
            req.setSuspendPolicy(EventRequest.SUSPEND_EVENT_THREAD);
            for (int i = 0; i < _excludes.length; ++i) {
                req.addClassExclusionFilter(_excludes[i]);
            }
            for (int i = 0; i < _includes.length; ++i) {
                req.addClassFilter(_includes[i]);
            }
            req.enable();
        }

        private void singleStepEvent(StepEvent event) {
            if (_passedCodeLines != null) {
                try {
                    final String sourcePath = event.location().sourcePath();
                    final int lineNumber = event.location().lineNumber();
                    final String method = event.location().method().toString();
                    final String lineKey = sourcePath + ":" + method  + ":" + lineNumber;
                    if (_lineStat.containsKey(lineKey)) {
                        Location location = _lineStat.get(lineKey);
                        location.countCall();
                    } else {
                        Location location = new Location(sourcePath, method, lineNumber);
                        location.countCall();
                        _lineStat.put(lineKey, location);
                    }
                    if (!_passedCodeLines.contains(lineKey)) {
                        _passedCodeLines.add(lineKey);
                    }
                } catch (AbsentInformationException e) {
                    e.printStackTrace();
                }
            } else {
                System.err
                        .println("Cannot set line numbers, because the container is null!");
            }
        }

        /**
         * Dispatch incoming events
         */
        private void handleEvent(Event event) {
            if (event instanceof StepEvent) {
                singleStepEvent((StepEvent) event);
            } else if (event instanceof VMStartEvent) {
                vmStartEvent((VMStartEvent) event);
            } else if (event instanceof VMDisconnectEvent) {
                vmDisconnectEvent((VMDisconnectEvent) event);
            } else if (event instanceof VMDeathEvent) {
                // application exit
            } else {
                System.out.println("Unhandled event type: " + event.getClass());
            }
        }

        private void handleDisconnectedException() {
            EventQueue queue = _vm.eventQueue();
            while (_connected) {
                try {
                    EventSet eventSet = queue.remove();
                    EventIterator iter = eventSet.eventIterator();
                    while (iter.hasNext()) {
                        Event event = iter.nextEvent();
                        if (event instanceof VMDisconnectEvent) {
                            vmDisconnectEvent((VMDisconnectEvent) event);
                        }
                    }
                    eventSet.resume();
                } catch (InterruptedException exc) {
                    // ignore
                }
            }
        }

        /**
         * Enable the SingleStepEvent if the VM was started in suspend mode.
         * @param event
         */
        private void vmStartEvent(VMStartEvent event) {
            EventRequestManager mgr = _vm.eventRequestManager();
            StepRequest req = mgr.createStepRequest(event.thread(),
                    StepRequest.STEP_LINE, StepRequest.STEP_INTO);
            req.setSuspendPolicy(EventRequest.SUSPEND_EVENT_THREAD);
            for (int i = 0; i < _excludes.length; ++i) {
                req.addClassExclusionFilter(_excludes[i]);
            }
            for (int i = 0; i < _includes.length; ++i) {
                req.addClassFilter(_includes[i]);
            }
            req.enable();
        }

        private void vmDisconnectEvent(VMDisconnectEvent event) {
            _connected = false;
        }

        @SuppressWarnings("unchecked")
        public static EventCatcherThread connectToVm(int port) throws Error,
                IOException, InterruptedException,
                IllegalConnectorArgumentsException {
            AttachingConnector c = getConnector();
            Map<String, Argument> arguments = c.defaultArguments();
            Argument portArg = arguments.get("port");
            portArg.setValue("" + port);
            // FIXME: localhost doesn't work
            Argument hostArg = arguments.get("hostname");
            hostArg.setValue("elaste");
            VirtualMachine myVM = c.attach(arguments);
            myVM.setDebugTraceMode(0);
            final String[] excludes = { "org.hibernate.*", "net.sf.cglib.*",
                    "org.junit.*", "java.*", "javax.*", "sun.*", "com.sun.*" };
            final String[] includes = { };
            EventCatcherThread eventThread = new EventCatcherThread(myVM, excludes,
                    includes);

            return eventThread;
        }

        private static AttachingConnector getConnector() {
            AttachingConnector result = null;
            List<AttachingConnector> allConnectors = Bootstrap
                    .virtualMachineManager().attachingConnectors();
            if (allConnectors.size() > 0) {
                result = allConnectors.get(0);
            }
            return result;
        }

        public void resumeVM() {
            _vm.resume();
        }

        public List<String> getPassedCodeLines() {
            return _passedCodeLines;
        }

        public void setPassedCodeLines(List<String> codeLines) {
            _passedCodeLines = codeLines;
        }

        public Location getLineStat(String lineKey) {
            return _lineStat.get(lineKey);
        }
    }
