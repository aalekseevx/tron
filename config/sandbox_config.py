SANDBOX = {
    "command": ["firejail", f"--profile={SANDBOX_PROFILE_PATH}"],
    "blacklisted_dirs": [
        '/bin',
        # '/usr',
        '/etc',
        '/lib32',
        '/sys',
        '/vmlinuz',
        '/boot',
        '/tmp'
        '/initrd.img',
        '/vmlinuz.old',
        '/dev',
        '/initrd.img.old',
        '/libx32',
        '/opt',
        '/sbin',
        '/lost+found',
        '/srv',
        '/var'
    ],

    "options": [
        'quiet',
        'read-only /',
        'disable-mnt',
        'apparmor',
        'caps.drop all',
        'seccomp',
        'memory-deny-write-execute',
        'nonewprivs',
        'noroot',
        'x11 none',
        'nodvd',
        'nogroups',
        'shell none',
        'nodbus',
        'nosound',
        'noautopulse',
        'notv',
        'nou2f',
        'novideo',
        'no3d',
        'net none'
    ],

    "rlimits": [
        # ML is 512 MB
        'rlimit-as 536870912',
        # TL is 1000 seconds
        'rlimit-cpu 1000',
        'rlimit-nproc 0',
        'rlimit-sigpending 0'
    ]
}