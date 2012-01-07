# -*- coding: UTF-8 -*-

import postmarkup
import unittest
  
class TestPostmarkup(unittest.TestCase):
        
    def test_textilize(self):
        """Test textilize function"""
        tests = [(u"<b>No bold</b>", u"No bold"),
                 (u'<span class="blah">A span</span>', u"A span"),
                 (u"Just text", u"Just text"),
                 (u"<p>paragraph</p>", u" paragraph")]
        
        for test, result in tests:
            self.assertEqual(postmarkup.textilize(test), result)
        
    def test_strip_bbcode(self):
        """Test strip_bbcode function"""
        tests = [(u"[b]Not bold[/b]", u"Not bold"),
                 (u"Just text", u"Just text"),
                 (u"[b][i][url][url=test]", u"")]
        
        for test, result in tests:
            self.assertEqual(postmarkup.strip_bbcode(test), result)
        
    def test_cleanuphtml(self):
        """Test cleanup_html"""
        markup = postmarkup.create()

        tests = [(u"""\n<p>\n </p>\n""", u""),
                 (u"""<b>\n\n<i>   </i>\n</b>Test""", u"Test"),
                 (u"""<p id="test">Test</p>""", u"""<p id="test">Test</p>"""),]

        for test, result in tests:
            self.assertEqual(markup.cleanup_html(test).strip(), result)


    def test_simpletag(self):
        "Test simple tags"
        markup = postmarkup.create()

        tests = [ (u'[b]Hello[/b]', u"<strong>Hello</strong>"),
                  (u'[i]Italic[/i]', u"<em>Italic</em>"),
                  (u'[s]Strike[/s]', u"<strike>Strike</strike>"),
                  (u'[u]underlined[/u]', u"<u>underlined</u>"),
                  ]

        for test, result in tests:
            self.assertEqual(markup(test), result)


    def test_overlap(self):
        """Test overlapping tags produce correct output"""
        markup = postmarkup.create()

        tests = [ (u'[i][b]Hello[/i][/b]', u"<em><strong>Hello</strong></em>"),
                  (u'[b]bold [u]both[/b] underline[/u]', u'<strong>bold <u>both</u></strong><u> underline</u>')
                  ]

        for test, result in tests:
            self.assertEqual(markup(test), result)

    def test_links(self):
        """Test links produce correct output"""
        markup = postmarkup.create(annotate_links=False)

        tests = [ (u'[link=http://www.willmcgugan.com]blog1[/link]', u'<a href="http://www.willmcgugan.com">blog1</a>'),
                  (u'[link="http://www.willmcgugan.com"]blog2[/link]', u'<a href="http://www.willmcgugan.com">blog2</a>'),
                  (u'[link http://www.willmcgugan.com]blog3[/link]', u'<a href="http://www.willmcgugan.com">blog3</a>'),
                  (u'[link]http://www.willmcgugan.com[/link]', u'<a href="http://www.willmcgugan.com">http://www.willmcgugan.com</a>')
                  ]

        for test, result in tests:
            self.assertEqual(markup(test), result)
    
    def test_unknowntags(self):
        """Test unknown tags pass through correctly"""
        markup = postmarkup.create(annotate_links=False)
        
        tests = [ (u'[REDACTED]', u'[REDACTED]'),
                  (u'[REDACTED this]', u'[REDACTED this]'),
                  (u'[REDACTED <b>]', u'[REDACTED &lt;b&gt;]') ]
        for test, result in tests:
            self.assertEqual(markup(test, render_unknown_tags=True), result)
    
    def test_unicode(self):
        """Test unicode support"""
        markup = postmarkup.create()

        tests= [ (u'[b]Hello André[/b]', u"<strong>Hello André</strong>"),
                 (u'[i]ɸβfvθðsz[/i]', u"<em>ɸβfvθðsz</em>"),                 
                 ]

        for test, result in tests:
            self.assertEqual(markup(test), result)
