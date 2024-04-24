# -*- mode: python -*-
# vim: ft=python

import sys


sys.setrecursionlimit(5000)  # required on Windows


a = Analysis(
    ['labelme/__main__.py'],
    pathex=['labelme-ytu'],
    binaries=[],
    datas=[
        ('labelme/config/default_config.yaml', 'labelme/config'),
        ('labelme/icons/*', 'labelme/icons'),
        ('labelme/translate/*.qm', 'translate'),
        ('ultralytics/default.yaml', 'ultralytics/cfg')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
)
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='labelme-ytu',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    icon='labelme/icons/icon.ico',
)
app = BUNDLE(
    exe,
    name='Labelme-YTU.app',
    icon='labelme/icons/icon.icns',
    bundle_identifier=None,
    info_plist={'NSHighResolutionCapable': 'True'},
)

coll = COLLECT(    
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Labelme-YTU',
)
