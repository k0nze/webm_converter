# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['webm_converter.py'],
             pathex=['C:\\Users\\konze\\Programming\\webm_conversion'],
             binaries=[('.\\ffmpeg.exe', '.\\ffmpeg')],
             datas=[('./images/logo_120x120.png', 'images'), ('./images/k_logo_30x30.png', 'images'), ('licenses', 'licenses')],
             hiddenimports=['PIL._tkinter_finder'],
             hookspath=[],
             hooksconfig={},
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
          name='webm_converter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='webm_converter')
