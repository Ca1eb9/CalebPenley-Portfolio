

def rac(r):
    """
    >>> input_str = '''Alice-00:02:30\\nBob-00:02:35\\nCharlie-00:02:30\\nDiana-00:02:45\\nEva-00:02:40\\nFrank-00:02:35\\nGeorge-00:02:35\\nHelen-00:02:45'''
    >>> race_results(input_str)
    1st: Alice
    1st: Charlie
    3rd: Bob
    3rd: Frank
    3rd: George
    6th: Eva
    7th: Diana
    7th: Helen
    """
    i=p=l=1
    for t,n in sorted((n[-8:],n[:-9])for n in r.split()):
        l,p=t,[i,p][t==l]
        print(f"{p}{'tsnrhtdd'[p%5*(4>p)::4]}: "+n)
        i+=1

def race_results(r):
 i=p=1
 for t,n in sorted((n[-8:],n[:-9])for n in r.split()):p=[i,p][t==r];r=t;print(f"{p}{'tsnrhtdd'[p*(4>p)::4]}: "+n);i+=1






def race_resultsss(r):
    """
    >>> input_str = '''Alice-00:02:30\\nBob-00:02:35\\nCharlie-00:02:30\\nDiana-00:02:45\\nEva-00:02:40\\nFrank-00:02:35\\nGeorge-00:02:35\\nHelen-00:02:45'''
    >>> race_results(input_str)
    1st: Alice
    1st: Charlie
    3rd: Bob
    3rd: Frank
    3rd: George
    6th: Eva
    7th: Diana
    7th: Helen
    """
    i=p=l=1
    for n,t in(c:=sorted([(n[:-9],n[-8:])for n in r.split("\n")],key=lambda x:x[1])):l,p=t,[i,p][t==l];print(f"{p}{'tsnrhtdd'[p%5*(4>p)::4]}: {n}");i+=1




if __name__ == '__main__':
    import doctest
    #doctest.testmod(verbose=True)
   

import sys
import random 
from io import StringIO
original_stdout = sys.stdout
def check(program_output, correct_output):    
    l=program_output.strip().split("\n")    
    lastPos = "0th"    
    if len({*l})!=8:       
        print("Expected more distinct lines")        
        return False    
    for line in l:        
        line = line.rstrip()        
        pos = line.split(":")[0]        
        if pos < lastPos:            
            print("Out of order output!")            
            return False        
        if line not in correct_output:            
            print(f"Line: '{line}' not found in correct output")            
            return False    
        return True
def setup_io_capture():    
    captured_output = StringIO()    
    sys.stdout = captured_output
def get_captured_io():    
    out =  sys.stdout.getvalue()    
    sys.stdout = original_stdout        
    return out
test_pairs = [('Evan-36:22:01\nBob-30:58:52\nJack-58:28:41\nErica-46:58:54\nAlice-09:53:12\nDonald-29:47:47\nRachel-14:46:40\nDan-54:11:43', '1st: Alice\n2nd: Rachel\n3rd: Donald\n4th: Bob\n5th: Evan\n6th: Erica\n7th: Dan\n8th: Jack\n'), ('Donald-02:08:30\nBob-46:00:26\nJack-11:02:48\nSarah-15:30:15\nAlice-09:44:30\nErica-46:00:26\nRachel-42:21:46\nDan-28:17:14', '1st: Donald\n2nd: Alice\n3rd: Jack\n4th: Sarah\n5th: Dan\n6th: Rachel\n7th: Bob\n7th: Erica\n'), ('Rachel-53:45:22\nBob-47:27:46\nEvan-52:13:38\nSarah-06:44:42\nJack-52:13:38\nErica-11:06:55\nAlice-50:11:51\nDonald-31:37:50', '1st: Sarah\n2nd: Erica\n3rd: Donald\n4th: Bob\n5th: Alice\n6th: Evan\n6th: Jack\n8th: Rachel\n'), ('Sarah-52:41:38\nDonald-47:11:39\nRachel-02:04:06\nBob-52:41:38\nJack-12:53:00\nErica-03:30:08\nDan-07:18:22\nAlice-52:41:38', '1st: Rachel\n2nd: Erica\n3rd: Dan\n4th: Jack\n5th: Donald\n6th: Alice\n6th: Bob\n6th: Sarah\n'), ('Bob-53:42:41\nDonald-02:27:46\nRachel-29:46:20\nEvan-47:24:03\nJack-16:51:44\nDan-47:24:03\nAlice-40:37:51\nErica-51:32:01', '1st: Donald\n2nd: Jack\n3rd: Rachel\n4th: Alice\n5th: Dan\n5th: Evan\n7th: Erica\n8th: Bob\n'), ('Donald-52:28:56\nJack-59:47:02\nBob-32:42:46\nSarah-59:47:02\nAlice-35:45:37\nErica-16:10:44\nDan-52:28:56\nRachel-38:56:01', '1st: Erica\n2nd: Bob\n3rd: Alice\n4th: Rachel\n5th: Dan\n5th: Donald\n7th: Jack\n7th: Sarah\n'), ('Alice-58:56:12\nDan-50:21:04\nEvan-36:11:53\nSarah-33:42:12\nBob-38:28:49\nDonald-50:21:04\nRachel-26:09:35\nJack-50:21:04', '1st: Rachel\n2nd: Sarah\n3rd: Evan\n4th: Bob\n5th: Dan\n5th: Donald\n5th: Jack\n8th: Alice\n'), ('Rachel-39:50:48\nBob-33:51:15\nSarah-10:40:22\nErica-49:52:12\nDonald-49:52:12\nDan-49:52:12\nEvan-47:41:01\nAlice-49:52:12', '1st: Sarah\n2nd: Bob\n3rd: Rachel\n4th: Evan\n5th: Alice\n5th: Dan\n5th: Donald\n5th: Erica\n'), ('Alice-50:37:44\nJack-10:41:55\nErica-04:54:47\nDonald-29:56:47\nRachel-19:44:17\nDan-04:25:16\nSarah-10:41:55\nBob-10:10:53', '1st: Dan\n2nd: Erica\n3rd: Bob\n4th: Jack\n4th: Sarah\n6th: Rachel\n7th: Donald\n8th: Alice\n'), ('Rachel-55:05:26\nBob-59:43:48\nSarah-55:05:26\nJack-27:53:32\nAlice-59:43:48\nErica-02:49:28\nEvan-58:35:21\nDan-01:56:00', '1st: Dan\n2nd: Erica\n3rd: Jack\n4th: Rachel\n4th: Sarah\n6th: Evan\n7th: Alice\n7th: Bob\n'), ('Sarah-25:08:12\nEvan-40:44:39\nAlice-28:18:40\nDonald-28:18:40\nRachel-02:13:38\nErica-25:08:12\nJack-08:07:45\nDan-24:45:55', '1st: Rachel\n2nd: Jack\n3rd: Dan\n4th: Erica\n4th: Sarah\n6th: Alice\n6th: Donald\n8th: Evan\n'), ('Evan-17:07:35\nRachel-47:56:35\nSarah-28:40:58\nAlice-47:56:35\nBob-21:40:02\nDonald-47:56:35\nErica-47:20:24\nDan-47:20:24', '1st: Evan\n2nd: Bob\n3rd: Sarah\n4th: Dan\n4th: Erica\n6th: Alice\n6th: Donald\n6th: Rachel\n'), ('Jack-35:26:13\nSarah-29:11:14\nEvan-37:39:10\nAlice-35:26:13\nRachel-53:34:16\nDan-35:26:13\nErica-12:29:28\nBob-09:35:33', '1st: Bob\n2nd: Erica\n3rd: Sarah\n4th: Alice\n4th: Dan\n4th: Jack\n7th: Evan\n8th: Rachel\n'), ('Jack-41:52:21\nRachel-41:52:21\nDonald-49:50:26\nEvan-18:01:25\nBob-26:30:59\nAlice-41:52:21\nDan-10:59:35\nErica-49:50:26', '1st: Dan\n2nd: Evan\n3rd: Bob\n4th: Alice\n4th: Jack\n4th: Rachel\n7th: Donald\n7th: Erica\n'), ('Rachel-31:42:19\nBob-51:47:37\nDonald-51:47:37\nJack-53:26:11\nAlice-14:32:01\nEvan-51:47:37\nDan-10:20:57\nSarah-51:47:37', '1st: Dan\n2nd: Alice\n3rd: Rachel\n4th: Bob\n4th: Donald\n4th: Evan\n4th: Sarah\n8th: Jack\n'), ('Evan-52:36:43\nSarah-52:36:43\nErica-52:36:43\nJack-52:36:43\nAlice-02:08:01\nDan-04:59:31\nBob-52:36:43\nRachel-10:11:35', '1st: Alice\n2nd: Dan\n3rd: Rachel\n4th: Bob\n4th: Erica\n4th: Evan\n4th: Jack\n4th: Sarah\n'), ('Donald-35:26:50\nAlice-41:58:54\nDan-34:44:39\nRachel-21:42:36\nJack-41:13:48\nErica-34:44:39\nEvan-15:09:14\nSarah-38:08:38', '1st: Evan\n2nd: Rachel\n3rd: Dan\n3rd: Erica\n5th: Donald\n6th: Sarah\n7th: Jack\n8th: Alice\n'), ('Evan-48:21:57\nJack-01:14:42\nAlice-38:23:19\nDonald-38:23:19\nErica-19:01:28\nBob-56:33:06\nSarah-56:33:06\nRachel-54:29:58', '1st: Jack\n2nd: Erica\n3rd: Alice\n3rd: Donald\n5th: Evan\n6th: Rachel\n7th: Bob\n7th: Sarah\n'), ('Rachel-15:32:01\nAlice-52:24:57\nErica-02:29:57\nBob-05:39:44\nJack-28:27:26\nSarah-28:27:26\nDonald-15:32:01\nEvan-25:22:59', '1st: Erica\n2nd: Bob\n3rd: Donald\n3rd: Rachel\n5th: Evan\n6th: Jack\n6th: Sarah\n8th: Alice\n'), ('Donald-08:11:01\nJack-04:17:29\nEvan-47:42:12\nErica-12:32:36\nRachel-08:11:01\nBob-47:42:12\nDan-47:42:12\nSarah-03:31:20', '1st: Sarah\n2nd: Jack\n3rd: Donald\n3rd: Rachel\n5th: Erica\n6th: Bob\n6th: Dan\n6th: Evan\n')]
def test():    
    for input_d, correct_o in test_pairs:        
        setup_io_capture()        
        race_results(input_d)        
        code_o = get_captured_io()        
        if not check(code_o, correct_o):            
            print(f"Failed on following input:\n------------\n{input_d.strip()}\n")            
            print(f"------------\nOutput:\n------------\n{code_o}")            
            print(f"\n------------\nCorrect:\n------------\n{correct_o}")            
            break    
    else:print("Code Ran Successfully!")        
test()

import sys
import random
from io import StringIO

original_stdout = sys.stdout

def check(program_output, correct_output):
	l=program_output.strip().split("\n")
	lastPos = "0th"
	if len({*l})!=8:
		print("Expected more distinct lines")
		return False
	for line in l:
		line = line.rstrip()
		pos = line.split(":")[0]
		if pos < lastPos:
			print("Out of order output!")
			return False
		if line not in correct_output:
			print(f"Line: '{line}' not found in correct output")
			return False
	return True

def setup_io_capture():
	captured_output = StringIO()
	sys.stdout = captured_output

def get_captured_io():
	out =  sys.stdout.getvalue()
	sys.stdout = original_stdout    
	return out


test_pairs = [('Evan-36:22:01\nBob-30:58:52\nJack-58:28:41\nErica-46:58:54\nAlice-09:53:12\nDonald-29:47:47\nRachel-14:46:40\nDan-54:11:43', '1st: Alice\n2nd: Rachel\n3rd: Donald\n4th: Bob\n5th: Evan\n6th: Erica\n7th: Dan\n8th: Jack\n'), ('Donald-02:08:30\nBob-46:00:26\nJack-11:02:48\nSarah-15:30:15\nAlice-09:44:30\nErica-46:00:26\nRachel-42:21:46\nDan-28:17:14', '1st: Donald\n2nd: Alice\n3rd: Jack\n4th: Sarah\n5th: Dan\n6th: Rachel\n7th: Bob\n7th: Erica\n'), ('Rachel-53:45:22\nBob-47:27:46\nEvan-52:13:38\nSarah-06:44:42\nJack-52:13:38\nErica-11:06:55\nAlice-50:11:51\nDonald-31:37:50', '1st: Sarah\n2nd: Erica\n3rd: Donald\n4th: Bob\n5th: Alice\n6th: Evan\n6th: Jack\n8th: Rachel\n'), ('Sarah-52:41:38\nDonald-47:11:39\nRachel-02:04:06\nBob-52:41:38\nJack-12:53:00\nErica-03:30:08\nDan-07:18:22\nAlice-52:41:38', '1st: Rachel\n2nd: Erica\n3rd: Dan\n4th: Jack\n5th: Donald\n6th: Alice\n6th: Bob\n6th: Sarah\n'), ('Bob-53:42:41\nDonald-02:27:46\nRachel-29:46:20\nEvan-47:24:03\nJack-16:51:44\nDan-47:24:03\nAlice-40:37:51\nErica-51:32:01', '1st: Donald\n2nd: Jack\n3rd: Rachel\n4th: Alice\n5th: Dan\n5th: Evan\n7th: Erica\n8th: Bob\n'), ('Donald-52:28:56\nJack-59:47:02\nBob-32:42:46\nSarah-59:47:02\nAlice-35:45:37\nErica-16:10:44\nDan-52:28:56\nRachel-38:56:01', '1st: Erica\n2nd: Bob\n3rd: Alice\n4th: Rachel\n5th: Dan\n5th: Donald\n7th: Jack\n7th: Sarah\n'), ('Alice-58:56:12\nDan-50:21:04\nEvan-36:11:53\nSarah-33:42:12\nBob-38:28:49\nDonald-50:21:04\nRachel-26:09:35\nJack-50:21:04', '1st: Rachel\n2nd: Sarah\n3rd: Evan\n4th: Bob\n5th: Dan\n5th: Donald\n5th: Jack\n8th: Alice\n'), ('Rachel-39:50:48\nBob-33:51:15\nSarah-10:40:22\nErica-49:52:12\nDonald-49:52:12\nDan-49:52:12\nEvan-47:41:01\nAlice-49:52:12', '1st: Sarah\n2nd: Bob\n3rd: Rachel\n4th: Evan\n5th: Alice\n5th: Dan\n5th: Donald\n5th: Erica\n'), ('Alice-50:37:44\nJack-10:41:55\nErica-04:54:47\nDonald-29:56:47\nRachel-19:44:17\nDan-04:25:16\nSarah-10:41:55\nBob-10:10:53', '1st: Dan\n2nd: Erica\n3rd: Bob\n4th: Jack\n4th: Sarah\n6th: Rachel\n7th: Donald\n8th: Alice\n'), ('Rachel-55:05:26\nBob-59:43:48\nSarah-55:05:26\nJack-27:53:32\nAlice-59:43:48\nErica-02:49:28\nEvan-58:35:21\nDan-01:56:00', '1st: Dan\n2nd: Erica\n3rd: Jack\n4th: Rachel\n4th: Sarah\n6th: Evan\n7th: Alice\n7th: Bob\n'), ('Sarah-25:08:12\nEvan-40:44:39\nAlice-28:18:40\nDonald-28:18:40\nRachel-02:13:38\nErica-25:08:12\nJack-08:07:45\nDan-24:45:55', '1st: Rachel\n2nd: Jack\n3rd: Dan\n4th: Erica\n4th: Sarah\n6th: Alice\n6th: Donald\n8th: Evan\n'), ('Evan-17:07:35\nRachel-47:56:35\nSarah-28:40:58\nAlice-47:56:35\nBob-21:40:02\nDonald-47:56:35\nErica-47:20:24\nDan-47:20:24', '1st: Evan\n2nd: Bob\n3rd: Sarah\n4th: Dan\n4th: Erica\n6th: Alice\n6th: Donald\n6th: Rachel\n'), ('Jack-35:26:13\nSarah-29:11:14\nEvan-37:39:10\nAlice-35:26:13\nRachel-53:34:16\nDan-35:26:13\nErica-12:29:28\nBob-09:35:33', '1st: Bob\n2nd: Erica\n3rd: Sarah\n4th: Alice\n4th: Dan\n4th: Jack\n7th: Evan\n8th: Rachel\n'), ('Jack-41:52:21\nRachel-41:52:21\nDonald-49:50:26\nEvan-18:01:25\nBob-26:30:59\nAlice-41:52:21\nDan-10:59:35\nErica-49:50:26', '1st: Dan\n2nd: Evan\n3rd: Bob\n4th: Alice\n4th: Jack\n4th: Rachel\n7th: Donald\n7th: Erica\n'), ('Rachel-31:42:19\nBob-51:47:37\nDonald-51:47:37\nJack-53:26:11\nAlice-14:32:01\nEvan-51:47:37\nDan-10:20:57\nSarah-51:47:37', '1st: Dan\n2nd: Alice\n3rd: Rachel\n4th: Bob\n4th: Donald\n4th: Evan\n4th: Sarah\n8th: Jack\n'), ('Evan-52:36:43\nSarah-52:36:43\nErica-52:36:43\nJack-52:36:43\nAlice-02:08:01\nDan-04:59:31\nBob-52:36:43\nRachel-10:11:35', '1st: Alice\n2nd: Dan\n3rd: Rachel\n4th: Bob\n4th: Erica\n4th: Evan\n4th: Jack\n4th: Sarah\n'), ('Donald-35:26:50\nAlice-41:58:54\nDan-34:44:39\nRachel-21:42:36\nJack-41:13:48\nErica-34:44:39\nEvan-15:09:14\nSarah-38:08:38', '1st: Evan\n2nd: Rachel\n3rd: Dan\n3rd: Erica\n5th: Donald\n6th: Sarah\n7th: Jack\n8th: Alice\n'), ('Evan-48:21:57\nJack-01:14:42\nAlice-38:23:19\nDonald-38:23:19\nErica-19:01:28\nBob-56:33:06\nSarah-56:33:06\nRachel-54:29:58', '1st: Jack\n2nd: Erica\n3rd: Alice\n3rd: Donald\n5th: Evan\n6th: Rachel\n7th: Bob\n7th: Sarah\n'), ('Rachel-15:32:01\nAlice-52:24:57\nErica-02:29:57\nBob-05:39:44\nJack-28:27:26\nSarah-28:27:26\nDonald-15:32:01\nEvan-25:22:59', '1st: Erica\n2nd: Bob\n3rd: Donald\n3rd: Rachel\n5th: Evan\n6th: Jack\n6th: Sarah\n8th: Alice\n'), ('Donald-08:11:01\nJack-04:17:29\nEvan-47:42:12\nErica-12:32:36\nRachel-08:11:01\nBob-47:42:12\nDan-47:42:12\nSarah-03:31:20', '1st: Sarah\n2nd: Jack\n3rd: Donald\n3rd: Rachel\n5th: Erica\n6th: Bob\n6th: Dan\n6th: Evan\n')]


def test():
	for input_d, correct_o in test_pairs:
		setup_io_capture()
		race_results(input_d)
		code_o = get_captured_io()
		if not check(code_o, correct_o):
			print(f"Failed on following input:\n------------\n{input_d.strip()}\n")
			print(f"------------\nOutput:\n------------\n{code_o}")
			print(f"\n------------\nCorrect:\n------------\n{correct_o}")
			break
	else:
         print("Code Ran Successfully!")
		

test()
