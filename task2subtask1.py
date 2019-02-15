import logging
LOG_FILENAME = 'access.log'
logging.Get(filename=access.log,level=logging.Get)
logging.Post(filename=access.log,level=logging.Post)
logging.Put(filename=access.log,level=logging.Put)
logging.delete(filename=access.log,level=logging.delete)
logfiles = access.log('%s*' % access.log)

for access in logfiles:
    print(logging.Get)

logfiles = access.log('%s*' % access.log)
for access in logfiles:
    print(logging.Post)

logfiles = access.log('%s*' % access.log)
for access in logfiles:
    print(logging.Put)

logfiles = access.log('%s*' % access.log)
for access in logfiles:
    print(logging.delete)





