VERSION = '0.0.6'
APPNAME = 'ux'

srcdir = '.'

def set_options(ctx):
  ctx.tool_options('compiler_cxx')
  ctx.tool_options('unittestt')

def configure(ctx):
  ctx.check_tool('compiler_cxx')
  ctx.check_tool('unittestt')	
  ctx.env.CXXFLAGS += ['-O2', '-Wall', '-g']

def build(bld):
  bld.recurse('src')
