# from exabgp.environment import getenv


# def profile():
#     env = getenv()

#     if env.profile.file == 'stdout':
#         profiled = 'Reactor(%s).run(%s, "%s")' % (str(configurations), str(validate), str(ROOT))
#         exit_code = profile.run(profiled)
#         __exit(env.debug.memory, exit_code)

#     if pid:
#         profile_name = "%s-pid-%d" % (env.profile.file, pid)
#     else:
#         profile_name = env.profile.file

#     notice = ''
#     if os.path.isdir(profile_name):
#         notice = 'profile can not use this filename as output, it is not a directory (%s)' % profile_name
#     if os.path.exists(profile_name):
#         notice = 'profile can not use this filename as output, it already exists (%s)' % profile_name

#     if not notice:
#         cwd = os.getcwd()
#         log.debug('profiling ....', 'reactor')
#         profiler = profile.Profile()
#         profiler.enable()
#         try:
#             exit_code = Reactor(configurations).run(validate, ROOT)
#         except Exception:
#             exit_code = Reactor.Exit.unknown
#             raise
#         finally:
#             from exabgp.vendoring import lsprofcalltree

#             profiler.disable()
#             kprofile = lsprofcalltree.KCacheGrind(profiler)
#             try:
#                 destination = profile_name if profile_name.startswith('/') else os.path.join(cwd, profile_name)
#                 with open(destination, 'w+') as write:
#                     kprofile.output(write)
#             except IOError:
#                 notice = 'could not save profiling in formation at: ' + destination
#                 log.debug("-" * len(notice), 'reactor')
#                 log.debug(notice, 'reactor')
#                 log.debug("-" * len(notice), 'reactor')
#             __exit(env.debug.memory, exit_code)
#     else:
#         log.debug("-" * len(notice), 'reactor')
#         log.debug(notice, 'reactor')
#         log.debug("-" * len(notice), 'reactor')
#         Reactor(configurations).run(validate, ROOT)
#         __exit(env.debug.memory, 1)
