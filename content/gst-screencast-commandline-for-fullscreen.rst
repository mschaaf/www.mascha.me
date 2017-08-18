gst screencast commandline for fullscreen
#########################################
:date: 2012-03-12 21:43
:author: infram
:category: Misc
:tags: fullscreen, gst, ogg, screencast, theora, vorbis
:slug: gst-screencast-commandline-for-fullscreen
:status: published

gst-launch-0.10 oggmux name=mux ! filesink location=/tmp/tmppUzJ\_f
istximagesrc name=videosource display-name=:0.0 screen-num=0 !
video/x-raw-rgb,framerate=10/1 ! videorate ! ffmpegcolorspace !
videoscale method=1 !
video/x-raw-yuv,width=1280,height=800,framerate=10/1 ! theoraenc ! queue
! mux. gconfaudiosrc name=audiosource ! audioconvert ! vorbisenc ! queue
! mux
