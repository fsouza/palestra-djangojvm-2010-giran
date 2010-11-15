from settings.development import *

SETTINGS_ROOT = PROJECT_ROOT
PROJECT_ROOT = SETTINGS_ROOT[0:SETTINGS_ROOT.find('/WEB-INF')]

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
