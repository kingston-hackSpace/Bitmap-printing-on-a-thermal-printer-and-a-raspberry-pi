import cups
conn = cups.Connection()
printers = conn.getPrinters()
printer_name = conn.getDefault()
file = "/home/kingston-hackspace/Desktop/test.jpg"
conn.printFile(printer_name, file, "test_print",{})
