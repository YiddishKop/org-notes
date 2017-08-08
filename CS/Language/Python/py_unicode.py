s = u'\u0627\u0644\u0639\u062a\u0629'
print(s)
# it will print  ا(cant display here, but can see in console) to console
# print to console is GOOD, BUT output to file is BAD
# -------------------------
# output = open('output_uni.txt', 'a')
# output.write(s)
# output.close()

# when you want to output unicode to a file
# you need encode raw unicode

encoded = s.encode()
print(encoded)

encoded2 = s.encode('utf-8')
print(encoded2)

output = open('output_uni.txt', 'a')
output.write(encoded,'b')
output.close()

###########################################
# Unicode in Python 2                     #
###########################################

# 1. computer can ONLY understantd bytes
# 2. unicode or ascii is info-format defined by human
# 3. from human to computer is encoding
# 4. 1 to 1, 1 human code has 1 encoding method
# 5. encoding: unicode,ascii --- utf-8 ---> bytes
# 6. decoding: bytes --- utf-8 ---> unicode,ascii

# ========================================
# two datatypes in python2: uncode and str
# ========================================
# unicode, type is <str>, code points have encode() method to turn into byte string
# utf-8,   type is <byte>,byte string have decode() method to turn into code points

# below is some code in ipython
# x is unicode, it's 'Code points', has encode() method
# y is utf8,    it's 'byte string', has decode() method

# In [200]: x = u'Hi \u2119\u01b4\u2602\u210c\xf8\u1f24'
# In [257]: type(x)
# Out[259]: unicode

# In [260]: len(x)
# Out[261]: 9 # means 9 code points

# In [262]: y = x.encode('utf-8')
# In [273]: y
# Out[273]: 'Hi \xe2\x84\x99\xc6\xb4\xe2\x98\x82\xe2\x84\x8c\xc3\xb8\xe1\xbc\xa4'
# In [274]: type(y)
# Out[298]: str
# In [275]: len(y)
# Out[299]: 19 # means 19 bytes


# In [274]: z = y.decode('utf-8')
# In [290]: z
# Out[290]: 'Hi ℙƴ☂ℌøἤ'

# ===============================
# unicode encode to ascii ERROR
# ===============================
# a = x.encode('ascii')
# ---------------------------------------------------------------------------
# UnicodeEncodeError                        Traceback (most recent call last)
# <ipython-input-308-3d15aa39cbed> in <module>()
# ----> 1 a = x.encode('ascii')

# ====================================================================
# but we can deal with ERROR with [replace, xmlcharrefreplace, ignore]
# ===================================================================
# a = x.encode('ascii', 'replace')
# In [321]: a
# Out[322]: b'Hi ??????'

# In [323]: a = x.encode('ascii', 'xmlcharrefreplace')
# In [333]: a
# Out[333]: b'Hi &#8473;&#436;&#9730;&#8460;&#248;&#7972;'

# In [334]: a = x.encode('ascii', 'ignore')
# In [341]: a
# Out[341]: b'Hi '


# ==================================
# utf-8 bytes decode to ascii, ERROR
# ==================================
# In [388]: b = y.decode('ascii')
# ---------------------------------------------------------------------------
# UnicodeDecodeError                        Traceback (most recent call last)
# <ipython-input-389-07bc666cffb0> in <module>()
# ----> 1 b = y.decode('ascii')

# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 3: ordinal not in range(128)


# =================================================
# but we can deal with ERROR with [replace, ignore]
# =================================================
# In [390]: b = y.decode('ascii', 'ignore')
# In [397]: b
# Out[397]: 'Hi '

# In [398]: b = y.decode('ascii', 'replace')
# In [402]: b
# Out[402]: 'Hi ����������������'


# =======================================
# Implicit conversion from bytes to ascii
# =======================================
# unicode + byteString => unicode
# >>> u'hello' + 'world'
#     u'hello world'

#   unicode + byteString
# = unicode + (byteString.decode('ascii'))
# = unicode + unicode # ascii included in unicode

# decode below is automatically, because the sysdefalut
# coding format is 'ascii' in python2
# >>> sys.getdefaultencoding()
#     ascii

# ============================================
# Implicit conversion ERROR from utf8 to ascii
# ============================================
# unicode + utf8 => ERROR

# >>> u'\u2108\u2119' + my_utf8
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2
# in position 0: ordinal not in range(128)

#   unicode + my_utf8
# = unicode + (my_utf8.decode('ascii'))
# Error, utf8 -> ascii will lose information


# In python ,all data when encount an unicode string ,will
# implicit convert with an ascii encoding, this is valid
# when all data is ascii coding and invalid when the
# data is not ascii --- it will throw an exception: UnicodeDecodeError


###########################################
# Unicode in Python 3                     #
###########################################

# python2: unicode vs. str
# python3: str     vs. bytes
# Different from python 2,
# unicode now is called 'str' not 'unicode' in python 2
# str in python 2 store bytes
# str in python 3 store code points
# 'str' in python 2 is a byte string
# 'str' in python 3 is a unicode string

# In [26]: my_string = 'hi \u2119\u01b4\u2602'

# In [54]: type(my_string)
# Out[56]: str

# In [57]: my_bytes = b'hello world'

# In [69]: type(my_bytes)
# Out[72]: bytes

# ============================================
# python3 will NOT implicitly convert
# ============================================

# 'hello' + b'world'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-5-610c59f1452f> in <module>()
# ----> 1 'hello' + b'world'

# TypeError: must be str, not bytes

# ===========================================
# mixing bytes and unicode is PAIN in python3
# ===========================================
# you must explicitly do conversion, between bytes and unicode


# ===========================================
# Reading files in python3
# ===========================================
# Data you get from files depends on how you opened it.
# python 2 has txt-mode and binary-mode for opening files.
# python 3, what you get from a read operation, depends on
# how you open the file

# 1. open with default, ---> unicode
# 2. open with binary,  ---> bytes

# when you get data back from Django or json module,
# they will do decoding automatically for you, so
# you get unicode directly
