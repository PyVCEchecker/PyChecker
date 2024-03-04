from texttable import Texttable                                                                                                              
tt = Texttable()                                                                                                                             
tt.set_cols_dtype(['i'])  # dtype 'i' is the problem here                                                                                    
tt.add_rows([['hello'], [18014398509481983]])                                                                                                
print(tt.draw())     
