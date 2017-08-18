The truth about traditional JavaScript benchmarks | Benedikt Meurer
###################################################################
:date: 2016-12-16 20:42
:author: infram
:category: Misc
:slug: the-truth-about-traditional-javascript-benchmarks-benedikt-meurer
:status: published

    We removed the so-called transcendental cache from V8 because the
    overhead of the cache was noticable in actual workloads where you
    don’t always compute the same values in a row, which is
    unsurprisingly very common in the wild.

http://benediktmeurer.de/2016/12/16/the-truth-about-traditional-javascript-benchmarks/
