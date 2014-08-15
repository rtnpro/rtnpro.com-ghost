.. link: 
.. description: 
.. tags: fedora, flock, waartaa
.. date: 2014/08/14 23:26:11
.. title: Flock 2014
.. slug: flock-2014

It was great that our proposal to speak on Waartaa at Flock, 2014 was accepted.
So, I, along with Sayan went to Prague, Czech Republic last week to attend
Flock. Flock was a 4 day event packed with loads of talks and workshops.
It was like living in a dream at Flock, where I met legends from the Fedora
community and Open Source community, about whom you have heard loads of awesome
stories and with whom I spoke online.

Day 1
*****
The day started with an opening note from Matthew Miller, the Fedora Project
Leader followed by a keynote by Gijs Hillenius on "Free and Open Source
Software in Europe: Policies and implementations". Gijs, an IT journalist,
threw light on the state of adoption of Open Source Software by the European
Union, it's success so far, things that did not work out and how politics
is playing a crucial role in the process. Then I attended the talk on
"Better presentation of fonts in Fedora" by Praveen Satpute. In the talk,
Praveen expressed his concerns on the lack of good tools to manage fonts and
that YUM is not sufficient for it. He laid emphasis on building a better
infrastructure for managing fonts. This will help to grow community around
fonts and better quality fonts in Fedora.

After this, I attended the talk on "Where's Wayland?" by Matthias Clasen.
Although, I could not make much out of the technical tits and bits of Wayland,
yet I got some insight into how Wayland plans to replace X11 and improve
application security in Gnome. After lunch, Hans de Geode spoke on
"Wayland Input Status". Here, I came to know about the complexities involved
in handling events from input devices: mouse, touchpad, etc. and how they are
evolving the input system for the upcoming Wayland integration. This was
followed by a talk on "Predictive Input Methods" by Anish and Mike.

Then, there was our (me and Sayan) talk on "Open communication and collaboration tool for
humans" where we spoke on the status quo in the field of communication and
collaboration tools and the lack of competent tools for the same in the Open
Source ecosystem. Then we showcased how we are trying to build a competent Open
Source tool for communication and collaboration, i.e., Waartaa, it's current
feature and it's roadmap. After our talk, I went to attend the talk on
Mailman 3's Hyperkitty by Aurelien Bompard, followed by the talk on "Fedora
Badges and Badge Design" by Marie and Chris. The day ended with a party
at "The Pub".

Day 2
*****
The second day started with Pierre-Yves Chibon(AKA pingou) and Stanislav Ochotnicky
speaking on the Fedora review server and how package review can happen without
any bugzilla interaction. This tool will speed up the process of package review
by eliminating time consuming to and fro communication between the package
maintainer and the reviewer. The tool will also include integration with
existing Fedora infra tools: FAS, koji, copr, etc. This was followed by an
awesome talk on Ansible and it's usage in Fedora Infra by Aditya Patawari.

This was followed by the keynote on Novenna, the open laptop project, by
Sean Cross. Sean spoke on how they built a laptop from scratch, how did the
project start, the architecture of the laptop and their roadmap.

The rest of day, I was busy hacking on Waartaa and speaking people about it.
Then, I attended the talk on "Rise of the Fedora Desktop: Gaming". I
recollected the days I spent tweaking Wine to run various Windows applications
and games on my Fedora box. I shared my good and bad experiences with gaming
on Linux with Gergely afte the talk.

The second day ended with an awesome boat party on the river Vltava.

Day 3 & 4
*********
Well, I spent most of the last 2 days of Flock hacking on Waartaa. In between,
I also attended quite a few talks and workshops. I started Day 3 by going to
the talk on "Gnome: a content application update" by Debarshi Ray, a Gnome
contributor and also one of my mentors in the world of Open Source. Then there
was the joint session on Fedora Next, where Matthew introduced the respective
project heads for different Fedora Next verticals. Each project head spoke
about what is coming up for this release, roadmap for future and where they
need helping hands. Then there was a group photo session before lunch. As
always, it was Jared who was taking the photographs, standing on the edge of a
window a couple of floors above ;)

After lunch, I went to listen to Richard Hughes speaking on building the Gnome
App installer from scratch. Following this, I attended the workshop on Fedmsg
by our dear and awesome threebean. Threebean started with showcasing the basic
API of fedmsg and finally went forward to implement a CLI based app which will
tweet when one votes for a package on Fedora tagger.

Following this I hanged around with Sarup and Marie, who were working on
designing a logo for Waartaa. Thanks a lot, folks :), now we have a logo for
Waartaa.

I started Day 4 by attending the talk on "Secure programming practices" by
huzaifas. Then I went to listen to Langdon White speak on
"Fedora for developers". Then I went to listen to Justin Forbes speak on how
to write kernel tests for Fedora. Post lunch, I resumed hacking again on Waartaa.
I also went to the Gnome newcomers workshop. I tried to add GIMPNet IRC server
in try.waartaa.com. However, it didn't work out as GIMPNet IRC server doesn't
seem to support SSL, whereas Waartaa in production enforces SSL connection to
IRC servers to ensure secure data transmission. I reported this issue to Marina.

Summary
*******
It was a wonderful experience to attend Flock. Meeting so many fellow open
source contributors, upstreams helped to strengthen my will of fire to contribute
more to the Open Source ecosystem. There are a few projects I badly want to
contribute to: Gnome, fedmsg, Mailman3, progit. But, I am currently too
overloaded with the tasks in Waartaa. I guess that's part and parcel of driving
your own project. I made quite some enhancements in Waartaa during the
conference. The important ones among them would be implementing route based
navigation in the chat interface, on demand loading of data, and bidirectional
pagination of chat logs (on going). This will help decreasing load time for
waartaa, decreasing client side memory usage and will provide a better mobile
experience. I spoke with Fedora infra team on various scale issues we are
currently facing with Waartaa and discussed on how to overcome them. I also
received a couple of feature requests for Waartaa. With support and feedback
from the community, I will keep making Waartaa better and better.

