# -*- mode: python -*-

block_cipher = None


a = Analysis(['__main__.py'],
             pathex=['/Users/cavidrzayev/Desktop/Projects/pyqtdjango'],
             binaries=None,
             datas=None,
             hiddenimports=['django.contrib.auth.apps', 'django.contrib.contenttypes.apps', 'apps.obj'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='__main__',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='__main__')
