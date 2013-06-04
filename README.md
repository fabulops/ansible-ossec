ansible-ossec
=============

OSSEC-HIDS agent management role for Ansible

This role is a reference implementation that you are free to use or
learn from (or complain about) for managing OSSEC-HIDS agents. Feel free
to contact me if you have questions or find me (asg) on freenode in
 #ansible. This implementation is Debian/Ubuntu specific but should only
require minimal changes to work with other *NIX variants.

Features
--------

   * Compiles the current (2.7) agent version from source
   * Will install compilers if they aren't already on the system and remove
     them if they were not already present.
   * Provides a default ossec.conf configuration with the option to
     override it on a per-host basis
   * Provides a default internal_options.conf configuration with the
     option to override it on a per-host basis
   * Provides a minimally tweaked init.d script to work with ansible
   * Automatically generates the client key
   * Automatically syncs the client key with the server

Requirements
------------

   * ansible 1.2 or greater
   * You'll need to have your ossec server setup already and its IP
     address set in group_vars/all. I'm working on a server role as
     well but it isn't currently available.
   * Assumes your server installation lives in /var/ossec
   * You'll need to make a /var/ossec/etc/keys directory to hold the
     sync'd client key fragments. If you have existing agents on the
     server, you'll also need to create a file for each (named by
     hostname) that contains the single line for that agent in
     /var/ossec/etc/client.keys
   * Your ansible command/control server needs to have python 2.5. If
     it doesn't, you'll need to modify filter_plugins/md5.py to use md5
     instead of hashlib

Caveats/Limitations
-------------------

   * The key id for each agent is the last octet of its ipv4 primary
     interface. This provides for 254 agents for each ossec server. If
     you have existing agents that don't conform to this scheme, you'll
     have to re-id your existing agents.
