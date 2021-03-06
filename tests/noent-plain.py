from errno import *

###############################################################################
#
# Attempted open of non-existent file; no special flags
#
###############################################################################

# Open read-only
def subtest_1(ctx):
    """Open O_RDONLY"""
    f = ctx.no_file() + ctx.termslash()

    ctx.open_file(f, ro=1, err=ENOENT)
    ctx.open_file(f, ro=1, err=ENOENT)

# Open write-only and overwrite
def subtest_2(ctx):
    """Open O_WRONLY"""
    f = ctx.no_file() + ctx.termslash()

    ctx.open_file(f, wo=1, err=ENOENT)
    ctx.open_file(f, wo=1, err=ENOENT)

# Open write-only and append
def subtest_3(ctx):
    """Open O_APPEND|O_WRONLY"""
    f = ctx.no_file() + ctx.termslash()

    ctx.open_file(f, app=1, err=ENOENT)
    ctx.open_file(f, app=1, err=ENOENT)

# Open read/write and overwrite
def subtest_4(ctx):
    """Open O_RDWR"""
    f = ctx.no_file() + ctx.termslash()

    ctx.open_file(f, rw=1, err=ENOENT)
    ctx.open_file(f, rw=1, err=ENOENT)

# Open read/write and append
def subtest_5(ctx):
    """Open O_APPEND|O_RDWR"""
    f = ctx.no_file() + ctx.termslash()

    ctx.open_file(f, ro=1, app=1, err=ENOENT)
    ctx.open_file(f, ro=1, app=1, err=ENOENT)
