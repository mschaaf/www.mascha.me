ClassCastException with SQLQuery and setCacheable(true)
#######################################################
:date: 2009-11-17 10:54
:author: infram
:category: Misc
:tags: ClassCastException, hibernate, Programming, query cache
:slug: classcastexception-with-sqlquery-and-setcacheabletrue
:status: published

Today I had to change a hibernate query constructed with the criteria
API to a SQL query. The result looked like:

``String sqlQuery = "select count(*) ..."; Session dbSession = getSession(); SQLQuery crit = dbSession.createSQLQuery(sqlQuery); crit.setCacheable(true); return (Integer) crit.uniqueResult();``

The former query was cached and the new one should be too. But I got the
following exception:

`` java.lang.ClassCastException: java.math.BigDecimal at org.hibernate.cache.StandardQueryCache.put(StandardQueryCache.java:83)``

The following `post from hibernate
forum <https://forum.hibernate.org/viewtopic.php?p=2391020>`__ helped me
to find a solution. The exception is gone after adding the result as a
scalar. And the working query looks like:

``String sqlQuery = "select count(*) as result ..."; Session dbSession = getSession(); SQLQuery crit = dbSession.createSQLQuery(sqlQuery); crit.addScalar("result", Hibernate.INTEGER); crit.setCacheable(true); return (Integer) crit.uniqueResult();``
