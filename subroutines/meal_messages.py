def bool_message(msg:str, type:bool=True, tag:str='p')->str:
    fa_class= {
        True: 'fas fa-check-circle',
        False: 'fa fa-times-circle',
    }[type] 
    color = {
        True:'green', 
        False:'red'
    }[type]
    return f'<{tag} style="background-color:black;color:white;padding:10px;"><span style="color:{color}" class="{fa_class}"></span> {msg}</{tag}>'