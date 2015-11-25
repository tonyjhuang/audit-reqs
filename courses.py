import sys

if len(sys.argv) != 2:
  print "Usage: python courses.py output_file_name"
  exit()

courses = "AFAM1101 1104 1109 1113 1140 1212 1270 2337 2338 2344 2399 4640 4710 4939 AFRS1101(FL13 OR AFTER) 1185 2307 3310 2348 3410 3424(FL14 OR AFTER) 3460 4500 ANTH1101 1220 2300 2302 2305 2315 2330 2350 2365 3412 OR LING3412 ANTH3415 4500 4505 4510 ARTH3410 4500 ARCH1310 1320 ARTH3410 ASNS1150 2245 BIOE3000(SP17 OR AFTER) CHME3000 CINE2550(THROUGH SP15) CLTR3450 CINE3450 3460 CIVE3000 CLTR1120 1500 1502 2501 1507 1240 1260 1280 2504 1503 1260 1265 1280 1501(S114 OR AFTER) 1504 1505 1575(FL14 OR AFTER) 2001 2475 2501 2504 2505 2715(SP15 OR AFTER) 2725(SP15 OR AFTER) 3450 3710(FL13 OR AFTER) 3715(FL13 OR AFTER) 3720(FL13 OR AFTER) 3725(FL13 OR AFTER) COMM1304(FL13-FL14) 2303 2304 3304(SP15 OR AFTER) CRIM1200 1400(FL16 OR AFTER) 1500 1600 DEAF1500 1550 2500 ECON1290 1291 1292 EDUC7335 EECE3000 ENGL2760(SP15 OR AFTER) 3100(FL13 OR AFTER) 3399(SP09) 3487(S113 OR AFTER) 4670 3671(THROUGH S214) 3672(THROUGH S214) 3673(THROUGH S214) 3674(THROUGH S214) 3675(THROUGH S214) HONR2200 HUSV2350 3560 HIST1150 1185 1206(FL13 OR AFTER) 1215(SP13 OR AFTER) 1218(SP14 OR AFTER) 1242(THROUGH S215) 1245(THROUGH S215) 1252 1253 1254 1281 1282(SP13 OR AFTER) 1290 1294 1389 1390(SP15 OR AFTER) 1500(FL13 OR AFTER) 2211(SP13 OR AFTER) 2300(SP15 OR AFTER) 2308(SP15 OR AFTER) 2313(THROUGH S215) 2348(SP13 OR AFTER) 2350 2351 2352 2372 2373(SP16 OR AFTER) 3330(SP16 OR AFTER) HLTH2302 5174 5280 HONR1200 HSCI1261 IE  3000 INSH2101(SP15 OR AFTER) INTB2202 3310(FL13 OR AFTER) INTL1215(SP16 OR AFTER) 3250(SP15 OR AFTER) 3300(SP15 OR AFTER) 4510(FL15 OR AFTER) 4937 4938 4939 4940 INTB1201 1203 1209 WMNS1103 2500 1271(SP14 OR AFTER) 3402(SP14 OR AFTER) LACS1220 ASNS2245 JWSS1285 1294(SP14 OR AFTER) 1575(FL14 OR AFTER) 2269 2300(SP15 OR AFTER) 2313(SP14 OR AFTER) 2431(SP14 OR AFTER) 3100(FL13 OR AFTER) LITR3501 LACS1261 EECE3000(FL08 OR AFTER) JRNL3300(SP15 OR AFTER) 5360 LING3442(FL14 OR AFTER) 3456(FL14 OR AFTER) MEIE3000 MATH2201 ME  3000 MSCR2325(SP13 OR AFTER) 3437(SP13 OR AFTER) MUSC1104 1106 1112 1128 1130 1131 1132 1139 1143(SP14 OR AFTER) 2313 3350 MUSI3401(SP15 OR AFTER) NRSG2210 PHIL1130 1290(FL14 OR AFTER) 2327 PHTH5120 POLS1155 2370 2375 2380 3415(SP15 OR AFTER) 3418(SP15 OR AFTER) 3442(SP15 OR AFTER) 3445(SP15 OR AFTER) 3450(SP15 OR AFTER) 3465(SP15 OR AFTER) 3475(SP15 OR AFTER) 3480(FL14 OR AFTER) 3485(FL14 OR AFTER) 3487 PSYC1204 2101(SP15 OR AFTER) PT  5135 5160 RELS1104 1110 1111(SP14 OR AFTER) 1220 1230 1231 1260 1270 1271 1272 1273 1275 1276 1280 1281(FL13 OR AFTER) 1285 1287 1290 2300 2313 2315 2394 2395 3390 3393 3395 3398 SOCL1103 1215(SP16 OR AFTER) 1240 1260 1270 1288 3402 3406 4520 4521 WMNS1185(SP14 OR AFTER) 1260(SP14 OR AFTER) 1304(SP14-FL15) 2259(FL14 OR AFTER) 2302(SP14 OR AFTER) 2304(SP14 OR AFTER) 2373(SP16 OR AFTER) 3304(SP16 OR AFTER)"


array = []     # final container for possible courses (with course num and subject)
subject = ""   # course subject
num = ""       # course number 
reading = True # are we in the middle of reading a course?
paren = False   # are we in paren?
for c in courses:
  # If we're in a paren, we can ignore everything until we get to the matching paren.
  if paren:
    if c == ')':
      paren = False
      num = ""
      continue

  elif c.isalpha():
    if reading:
      subject += c
    else: # if we weren't already reading a course subject, then we've hit a new one
      subject = c
      reading = True
  elif c.isdigit():
    num += c
  if c.isspace():
    # if we're not in a paren and we hit a space, we should add the course to array
    reading = False
    if num: # num might be empty here, as it gets cleared out if we had hit a paren prior.
      array.append((subject, num))
      num = "" # clear out the number now that we're done with it
  elif c == '(':
    paren = True

# regex stuff
import urllib
import re
p = re.compile("<.*>.* - (.*)</TD>")
url = "https://wl11gp.neu.edu/udcprod8/bwckctlg.p_disp_course_detail?cat_term_in=201630&subj_code_in={0}&crse_numb_in={1}"

# Get progress bar ready.
import time
toolbar_width = len(array) / 2
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
progress = False # shrinks progress bar to len(array) / 2

# file I/o
out = open(sys.argv[1], "w")

for course in array:
  page = urllib.urlopen(url.format(course[0], course[1])).read()
  match = p.findall(page)
  if match:
    out.write(course[0] + course[1] + ": " + match[0] + '\n')
  if progress:
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()
  progress = not progress

sys.stdout.write("\n")
