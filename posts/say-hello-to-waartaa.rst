.. link: 
.. description: 
.. tags: waartaa, irc, meteor, communicate
.. date: 2013/12/10 02:52:27
.. title: Waartaa - IRC client as a service
.. slug: waartaa-irc-client-as-a-service

What is Waartaa?
================

**Waartaa** or **wārtā** is a word in Hindi: **वार्ता**, which means **to communicate**. And that's what *waartaa* is for. *Waartaa* is a web based **IRC** client as a service and it facilitates centralized logging, idling functionality, unique identification across multiple clients and a rich UI for awesome user experience. *Waartaa* is open sourced under *MIT License*. The source is at `https://github.com/waartaa/waartaa/ <https://github.com/waartaa/waartaa>`_
.You can download, fork, customize and setup *Waartaa* as a service anywhere, be it a single user laptop/desktop, server for your self and your friends.

.. image:: galleries/waartaa/waartaa.png
   :width: 90%
   :align: center


Why?
====
There are an arsenal of IRC clients and tools, so why another one?

Waartaa is not just a random fun project, although it has been fun and full of adventures to work on it. Below are a few reasons why I started to work on Waartaa:

* GUI IRC clients work only for single machines. It's a pain to sync logs across multiple devices across multiple IRC clients.
* Local IRC clients do not let you *idle* when you are not online. It's not possible for everyone to get a server to setup ZNC or similar idling server.
* Most desktop IRC clients do not have that WOW! look and feel.
* Lack of identity when logged in from multiple devices simultaneously.
* Local network configuration (proxy, firewall) and quality (speed, timeout) often becomes a hindrance to good IRC experience.

Waartaa solves the above issues as follows:

* Running IRC client as a service on better infrastructure ensures that you are always connected to IRC and capturing IRC logs.
* Waartaa serves as a central place to store your chat logs.
* No matter what device you login from to Waartaa, YOU are always YOU in the IRC and not some YOU\_, YOU\_\_, etc.
* Waartaa is built on top of web technologies. So, it works flawlessly and uniformly across multiple platforms and looks equally awesome in all the them. This adds up to a superior user experience.

Features
========

Beautiful and useful chat interface
-----------------------------------

.. container:: row

    .. container:: col-md-8

        .. image:: galleries/waartaa/waartaa_chat_logs.png
            :width: 100%
            :align: center

    .. container:: col-md-4

        .. image:: galleries/waartaa/waartaa_nick_options.png
            :width: 100%
            :align: center

Easy to join server/channel
---------------------------

.. container:: row

    .. container:: col-md-6

        .. image:: galleries/waartaa/waartaa_add_server.png
            :width: 100%
            :align: center

    .. container:: col-md-6

        .. image:: galleries/waartaa/waartaa_channel_join.png
            :width: 100%
            :align: center

Stylish menus
-------------

.. container:: row

    .. container:: col-md-4

        .. image:: galleries/waartaa/waartaa_server_menu.png
            :width: 100%
            :align: center

    .. container:: col-md-4

        .. image:: galleries/waartaa/waartaa_channel_menu.png
            :width: 100%
            :align: center

    .. container:: col-md-4

        .. image:: galleries/waartaa/waartaa_channel_nick_menu.png
            :width: 100%
            :align: center


Informative
-----------

.. container:: row

    .. container:: col-md-3

        .. image:: galleries/waartaa/waartaa_channel_connecting.png
            :width: 100%
            :align: center

    .. container:: col-md-3 col-md-offset-1

        .. image:: galleries/waartaa/waartaa_channel_unread_msg_count.png
            :width: 100%
            :align: center



Under the hood
================

1. **Meteor JS** `http://www.meteor.com/ <http://www.meteor.com/>`_
2. **MongoDB**
3. Forked **node-irc** `https://github.com/waartaa/node-irc <https://github.com/waartaa/node-irc>`_
4. And a host of meteorite apps from `https://atmosphere.meteor.com/ <https://atmosphere.meteor.com/>`_


Where can I try it?
===================

`https://waartaa-dev.nodejitsu.com/ <https://waartaa-dev.nodejitsu.com>`_

How can I contribute?
=====================

* Fork the code from `https://github.com/waartaa/waartaa <https://github.com/waartaa/waartaa>`_
* Setup as instructed in ``README``
* Start using it
* Report any issue at `https://github.com/waartaa/waartaa/issues/new <https://github.com/waartaa/waartaa/issues/new>`_
* Pick up issues to fix from `https://github.com/waartaa/waartaa/issues <https://github.com/waartaa/waartaa/issues>`_

