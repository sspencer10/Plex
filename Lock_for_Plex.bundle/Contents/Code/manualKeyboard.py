class manualKeyboard:

        #KEYS = list('0123456789')

        def __init__(self, prefix, oc, callback, mktitle=None, mkthumb=None, **kwargs):

                Route.Connect(prefix+'/manualKeyboard',                     self.Keyboard)
                Route.Connect(prefix+'/manualKeyboard/submit',              self.Submit)

                oc.add(DirectoryObject(
                        key   = Callback(self.Keyboard),
                        title = str(mktitle) if mktitle else u'%s' % L('Enter Password PIN'),
                        thumb = mkthumb
                ))

                self.Callback = callback
                self.callback_args = kwargs

        def Keyboard(self, query=None):

			oc = ObjectContainer()
			oc.add(DirectoryObject(key = Callback(self.Submit, query=query), title = u'%s: %s' % (L('Enter PIN'), query.replace(' ', '_') if query else query), thumb=R('enter.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'1' if query else 1), title = u'%s' % '', thumb=R('one.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'2' if query else 2), title = u'%s' % '', thumb=R('two.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'3' if query else 3), title = u'%s' % '', thumb=R('three.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'4' if query else 4), title = u'%s' % '', thumb=R('four.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'5' if query else 5), title = u'%s' % '', thumb=R('five.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'6' if query else 6), title = u'%s' % '', thumb=R('six.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'7' if query else 7), title = u'%s' % '', thumb=R('seven.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'8' if query else 8), title = u'%s' % '', thumb=R('eight.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'9' if query else 9), title = u'%s' % '', thumb=R('nine.png'),))
			oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query+'0' if query else 0), title = u'%s' % '', thumb=R('zero.png'),))
					
			if query:
				oc.add(DirectoryObject(key = Callback(self.Keyboard, query=query[:-1]),title = 'Backspace', thumb=R('backspace.png'),))
				
                

			if query:
			   if len(query) == 4:
				kwargs = {'query': query}
				kwargs.update(self.callback_args)
				return self.Callback(**kwargs)

			return oc

        def Submit(self, query):

                kwargs = {'query': query}
                kwargs.update(self.callback_args)
                
                return self.Callback(**kwargs)