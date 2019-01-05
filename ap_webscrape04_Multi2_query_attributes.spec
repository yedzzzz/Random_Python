# -*- mode: python -*-

block_cipher = None


a = Analysis(['ap_webscrape04_Multi2_query_attributes.py'],
             pathex=['D:\\Personal\\RnD\\Python\\ap_webscrape04_Multi2_query_attributes'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ap_webscrape04_Multi2_query_attributes',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
