from burp import IBurpExtender
from burp import IHttpListener
from burp import ITab
from burp import IContextMenuFactory
from javax.swing import JMenuItem, JDialog, WindowConstants, JPanel, JLabel, JComboBox
from java.awt import GridBagLayout

class PayloadsTab(ITab):
    
    def __init__(self, name, payloads):
        self.name = name
        self.payloads = payloads
    
    def getTabCaption(self):
        return self.name
    
    def getUiComponent(self):
        panel = JPanel(GridBagLayout())
        
        for i, payload in enumerate(self.payloads):
            label = JLabel("Payload " + str(i + 1))
            combo = JComboBox(payload)
            for p in payload:
                combo.addItem(p)
            panel.add(label)
            panel.add(combo)
        
        return panel

class PayloadsContextMenuFactory(IContextMenuFactory):
    
    def __init__(self, name, payloads):
        self.name = name
        self.payloads = payloads
    
    def createMenuItems(self, invocation):
        menuItems = []
        menuItem = JMenuItem(self.name)
        menuItem.addActionListener(lambda event: self.showPayloadsDialog(invocation))
        menuItems.append(menuItem)
        return menuItems
    
    def showPayloadsDialog(self, invocation):
        # Extract the selected message from the invocation
        selectedMessage = invocation.getSelectedMessages()[0]
        
        # Extract the request from the selected message
        request = selectedMessage.getRequest()
        
        # TODO: Implement your logic to show the payloads dialog and perform actions on the request
        
        # Example: Show payloads dialog
        payloads_dialog = PayloadsDialog(self.name, self.payloads)
        payloads_dialog.setVisible(True)

class PayloadsDialog(JDialog):
    
    def __init__(self, name, payloads):
        self.name = name
        self.payloads = payloads
        self.initUI()
    
    def initUI(self):
        self.setTitle(self.name)
        self.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
        
        panel = JPanel(GridBagLayout())
        
        for i, payload in enumerate(self.payloads):
            label = JLabel("Payload " + str(i + 1))
            combo = JComboBox(payload)
            for p in payload:
                combo.addItem(p)
            panel.add(label)
            panel.add(combo)
        
        self.add(panel)
        self.pack()
        self.setLocationRelativeTo(None)

class BurpExtender(IBurpExtender, IHttpListener):
    
    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Payloads Extension")
        callbacks.registerHttpListener(self)
        
        # Define payloads for each vulnerability
        xss_payloads = [
            '"><img src=x onerror=alert(1)></img>',
            '<svg onload=alert(1)></svg>',
            '<h1>hai</h1>'
        ]
        
        sql_injection_payloads = [
            "'",
            "or'1'='1"
        ]
        
        # Create the payload tabs
        xss_tab = PayloadsTab("XSS Payloads", [xss_payloads])
        sql_injection_tab = PayloadsTab("SQL Injection Payloads", [sql_injection_payloads])
        
        # Add the tabs to Burp's UI
        callbacks.addSuiteTab(xss_tab)
        callbacks.addSuiteTab(sql_injection_tab)

        # Create the context menu items
        xss_context_menu = PayloadsContextMenuFactory("XSS Payloads", [xss_payloads])
       
