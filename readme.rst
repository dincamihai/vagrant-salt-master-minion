How to view beacon data: `sudo salt-run state.event pretty=true`

How to remove update lockfile (stuck gitfs):

- `sudo salt-run cache.clear_git_lock gitfs`
- https://docs.saltstack.com/en/latest/topics/tutorials/gitfs.html#why-aren-t-my-custom-modules-states-etc-syncing-to-my-minions
- sometimes works after runing `vagrant provision` again

How to refresh beacons: `sudo salt '*' saltutil.refresh_beacons`

Master gitfs cache location: `/var/cache/salt/master/gitfs/refs/`

Minion cached beacons location: `/var/cache/salt/minion/extmods/_beacons`
