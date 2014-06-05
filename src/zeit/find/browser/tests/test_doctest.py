# Copyright (c) 2009-2010 gocept gmbh & co. kg
# See also LICENSE.txt

import zeit.cms.testing
import zeit.find.tests


def test_suite():
    return zeit.cms.testing.FunctionalDocFileSuite(
        'README.txt',
        package='zeit.find.browser',
        layer=zeit.find.tests.LAYER)
