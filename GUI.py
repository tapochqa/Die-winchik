# -*- coding: utf-8 -*- 

import subprocess
import wx


import wx.xrc


def pacclist():
	flist = []
	with open('logins', 'r') as logins:
		for line in logins:
			lnd = line.split(':')
			flist.append(lnd[0])
	return flist
	
class Window ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Дай Винчик сука", pos = wx.DefaultPosition, size = wx.Size( 520,470 ), style = wx.DEFAULT_FRAME_STYLE|wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		loginbox = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Логин" ), wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText5 = wx.StaticText( loginbox.GetStaticBox(), wx.ID_ANY, u"Логин", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.blogin = wx.TextCtrl( loginbox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.blogin, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( loginbox.GetStaticBox(), wx.ID_ANY, u"Пороль", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.bpassword = wx.TextCtrl( loginbox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer3.Add( self.bpassword, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		acclistChoices = pacclist()
		self.acclist = wx.ListBox( loginbox.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, acclistChoices, wx.LB_ALWAYS_SB )
		bSizer2.Add( self.acclist, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		self.delacc = wx.Button( loginbox.GetStaticBox(), wx.ID_ANY, u"Удалить аккаунт", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.delacc, 0, wx.ALIGN_BOTTOM|wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		self.addacc = wx.Button( loginbox.GetStaticBox(), wx.ID_ANY, u"Добавить аккаунт", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.addacc, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		loginbox.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( loginbox, 1, wx.ALIGN_CENTER, 5 )
		
		logbox = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Лог" ), wx.VERTICAL )
		
		self.log = wx.TextCtrl( logbox.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		logbox.Add( self.log, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.SHAPED, 5 )
		
		
		bSizer1.Add( logbox, 1, wx.EXPAND, 5 )
		
		self.starter = wx.Button( self, wx.ID_ANY, u"ДАЙ ВИНЧИК", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.starter, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.status = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.delacc.Bind( wx.EVT_BUTTON, self.delete_account )
		self.addacc.Bind( wx.EVT_BUTTON, self.add_account )
		self.starter.Bind( wx.EVT_BUTTON, self.bot_start )
		self.log.Bind( wx.EVT_UPDATE_UI, self.refresh )
		
		#show
		self.Show(True)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def delete_account( self, event ):
		l =  open('logins', 'r')
		k = l.readlines()
		l.close()
		for account in k:
			if account.find(self.acclist.GetString(self.acclist.GetSelection())) != -1:
				k.remove(account)
		l = open('logins', 'w')
		l.writelines(k)
		l.close()
		self.acclist.Delete(self.acclist.GetSelection())
		
	
	def add_account( self, event ):
		acc = open('logins', 'a')
		acc.write(self.blogin.Value + ':' + self.bpassword.Value+'\n')
		acc.close()
		self.acclist.Append(self.blogin.Value)
		self.blogin.Value = ''
		self.bpassword.Value = ''
	
	def bot_start( self, event ):
		with open('work', 'w') as work:
			work.write('1')
		
		p=subprocess.Popen('main.py', shell=True, stdout = subprocess.PIPE)
		self.starter.Bind( wx.EVT_BUTTON, self.bot_stop )
		self.starter.SetLabel(u'СТОП')
		self.addacc.Disable()
		self.delacc.Disable()
		
	def bot_stop( self, event ):
		with open('work', 'w') as work:
			work.write('0')
		work = False
		self.starter.SetLabel(u'ДАЙ ВИНЧИК')
		self.addacc.Enable()
		self.delacc.Enable()
		self.starter.Bind( wx.EVT_BUTTON, self.bot_start )
		
	
	def refresh( self, event ):
		o=open('logs', 'r')
		self.log.SetLabel (o.read())
		o.close()

app = wx.App()
wnd = Window(None)
app.MainLoop()