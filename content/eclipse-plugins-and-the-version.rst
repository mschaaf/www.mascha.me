Eclipse plugins and the version
###############################
:date: 2008-02-18 09:27
:author: infram
:category: Misc
:tags: eclipse, not updated, plugins, Programming
:slug: eclipse-plugins-and-the-version
:status: published

Trouble with installed plugins that aren't update completly if you do
not change the version number? But you do not want to set it higher for
every test. Then it helps to use the qualifier. Set the version string
fo your plugins as follow 1.2.3.qualifier and on deploying disable
qualifier replacement with a static string under the options tab. Voila.
Eclipse will replace the qualifier string with the current timestamp on
every deployment.
