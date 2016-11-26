# -*- mode: python -*-

block_cipher = None


a = Analysis(['OpenJournal.py'],
             pathex=['C:\\Users\\Chris\\AppData\\Local\\Programs\\Python\\Python35-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'Y:\\Documents\\OneDrive\\Code\\OpenJournal'],
             binaries=[],
             datas=[],
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
          console=False , icon='logos\\OpenJournal_Windows.ico')
