print('python3 package relative import is shit!!!')
print(__package__)

if __package__ is None or __package__ == '':
#uses current directory visibility
  from editor import slider
else:
#uses current package visibility
  from .editor import slider



slider.test_func()