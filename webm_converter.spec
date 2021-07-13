# -*- mode: python ; coding: utf-8 -*-

from consts import *

block_cipher = None


a = Analysis([FILE_NAME + '.py'],
             pathex=['./webm_converter'],
             binaries=[],
             datas=[('./images/logo_120x120.png', 'images'), ('./images/k_logo_30x30.png', 'images')],
             hiddenimports=['PIL._tkinter_finder'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=FILE_NAME,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=FILE_NAME)

