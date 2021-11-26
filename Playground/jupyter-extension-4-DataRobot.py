
# 02:33 2021/11/22 was 'forth.py' 
# Usage: %run ../../../jupyter-extension.py 
#        In a jupyternotebook cell to init peforth

print(__file__)
import peforth
peforth.dictate(
    '''
    ' paste [if] 
        .( 煩不煩？已經執行過了！ ) cr stop 
    [else]
        import IPython
        : paste py> IPython.lib.clipboard.win32_clipboard_get() tib.insert ;
            // ( ... -- ... ) 執行 clipboard 裡的內容，jupyternotebook 進了 peforth prompt 特別需要此功能。
        char https://app.datarobot.com/api/v2 constant endpoint // ( -- url ) 
        char NjBiNzQzMzA3NWVkNjdhNjhjM2M4Y2RkOkZSS0RTL1lYaUE1WWRZbU5Ka1gwb1YvM3lHTmc3ZVByeXErUGo0SmZpOHc9 constant api_token // ( -- str ) DataRobot's API Token
    [then] 
    '''
)
