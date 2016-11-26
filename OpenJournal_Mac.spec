# -*- mode: python -*-

block_cipher = None


a = Analysis(['OpenJournal.py'],
             pathex=['Y:\\Documents\\OneDrive\\Code\\OpenJournal'],
             binaries=None,
             datas=None,
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='OpenJournal',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='logos\\OpenJournal_Windows.ico')
app = BUNDLE(exe,
             name='OpenJournal.app',
             icon='logos/OpenJournal_ICO.icns',
             bundle_identifier=None,
             info_plist={
                'NSHighResolutionCapable': 'True'
                },
             )
