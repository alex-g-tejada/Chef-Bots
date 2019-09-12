touchApp = runTouchApp(Builder.load_string('''
    StackLayout:
        Label:
            text:'S1'
'''))

kv_str = Builder.load_string('''
    ActionBar:
        pos_hint: {'pip top':1}
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'Chef Bots'
                with_previous: False
            ActionButton:
                text: 'Login'
            ActionGroup:
                text: 'Tools' 
                mode: 'spinner'
                ActionButton:
                    text: 'Tool1'
                ActionButton:
                    text: 'Tool2'
                ActionButton:
                    text: 'Tool3'
                ActionButton:
                    text: 'Tool4'
''')