.. title: Waartaa stats
.. slug: waartaa-stats
.. date: 2014-10-27 08:41:48 UTC+05:30
.. tags: waartaa, irc, Fedora, meteorjs
.. link: 
.. description: Stats of try.waartaa.com
.. type: text

`try.waartaa.com <https://try.waartaa.com>`_ has been live since January, 2014. We have
got quite some signups and some folks actively using Waartaa. Thanks to our code level
optimizations, which has led to storage complexity for channel chat logs dependent only
number of unique channels being listened to. We're also able to achieve good real time
performace in our demo instance with ever growing chat logs. It's time to publish some
stats about our demo instance.

Resources
=========

- Application server

  Specs: 2 CPUs, 2 GB RAM (Linode VPS)
  Usage:

  - CPU: around 5%
  - RAM: between 150 to 200 MB
- Database(Mongodb) server

  Specs: 8 CPUs, 2 GB RAM (Linode VPS)
  Usgae:

  - CPU: less than 2%
  - RAM: around 1.2 GB


Reports
=======

.. chart:: StackedLine
   :title: 'User signups'
   :x_labels: ["Jan'14", "Feb'14", "Mar'14", "Apr'14", "May'14", "Jun'14", "Jul'14", "Aug'14", "Sep'14", "Oct'14"]
   :human_readable: True
   :width: 600
   :height: 300

   'count/month', [27, 63, 121, 19, 32, 56, 111, 70, 48, 28]
   'cumulative count', [27, 90, 211, 230, 262, 318, 429, 499, 547, 575]

.. chart:: StackedLine
   :title: 'Channel chat log stats'
   :x_labels: ["Jan'14", "Feb'14", "Mar'14", "Apr'14", "May'14", "Jun'14", "Jul'14", "Aug'14", "Sep'14", "Oct'14"]
   :human_readable: True
   :width: 600
   :height: 300

   'count/month', [133252, 828002, 3670352, 567459, 527310, 1277257, 2491575, 2932374, 2654422, 1414509]
   'cumulative count', [133252, 961254, 4631606, 5199065, 5726375, 7003632, 9495207, 12427581, 15082003, 16496512]

