# -*- mode: python -*-

block_cipher = None


a = Analysis(['main_gui.py'],
             pathex=['D:\\school\\3Class_1Step\\script\\script - บนป็บป\\team'],
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
          name='main_gui',
          debug=False,
          strip=False,
          upx=True,
          console=True )
