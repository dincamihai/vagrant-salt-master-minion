Description:

This is a vagrant configuration file that would create a vagrant machine with master-minion salt configuration.
The minion key is pre-accepted by the master (that's why the keys are shipped in this repo).

The *top-file* is served using the built-in salt file server while the rest of the sls files are served using *gitfs* from the `SLS files repo`_.

A beacon reporting the CPU% is also installed on the minion. The beacon is served using *gitfs* from `CPU beacon repo`_.

Installation:

.. code-block:: bash

   git clone https://github.com/dincamihai/vagrant-salt-master-minion saltstack_vagrant
   cd saltstack_vagrant
   vagrant up
   vagrant provision # because the beacon does not work right away

To see beacon data:

.. code-block:: bash

   vagrant ssh
   sudo salt-run state.event pretty=true # to see the data coming from the beacon


Explanation:

``vagrant provision`` is required after ``vagrant up`` because there are some issues with *gitfs* when using *GitPython* gitfs provider (please see `GitPython issues`_ page)
Sometimes ``vagrant provision`` doesn`t solve the problem. I've managed to overcome this by doing the following:

.. code-block:: bash

   vagrant ssh
   sudo salt-run cache.clear_git_lock gitfs # to remove the update lockfile caused by the errors raised by *GitPython*
   sudo salt '*' saltutil.refresh_beacons # to trigger update the minion beacon cache
   sudo service salt-minion restart
   sudo salt-run state.event pretty=true # to check if the beacon is working

Where to check in case nothing works:

    - Master gitfs cache location: `/var/cache/salt/master/gitfs/refs/`
    - Minion cached beacons location: `/var/cache/salt/minion/extmods/_beacons`


.. _SLS files repo: https://github.com/dincamihai/saltstack_root

.. _CPU beacon repo: https://github.com/dincamihai/cpu_beacon

.. _GitPython issues: https://docs.saltstack.com/en/latest/topics/tutorials/gitfs.html#why-aren-t-my-custom-modules-states-etc-syncing-to-my-minions
