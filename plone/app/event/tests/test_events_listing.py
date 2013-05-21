from plone.app.event.base import localized_today
from plone.app.event.dx.behaviors import EventAccessor as DXEventAccessor
from plone.app.event.testing import PAEventDX_INTEGRATION_TESTING
from plone.app.event.tests.base_setup import AbstractSampleDataEvents

import logging


logger = logging.getLogger(name="plone.app.event test_events_listing")


class TestEventsListingDX(AbstractSampleDataEvents):
    layer = PAEventDX_INTEGRATION_TESTING

    def event_factory(self):
        return DXEventAccessor.create

    # TODO: mock base functions localized_now and start_end_from_mode to get
    # reproducable results. Currently, tests fail if we catch a leap second.

    def test_get_events_future(self):
        # Default mode is to show all events from now on.
        view = self.portal.restrictedTraverse('@@event_listing')
        self.assertEqual(len(view._get_events()), 5)

    def test_get_events_past(self):
        self.request.form.update({'mode': 'past'})
        view = self.portal.restrictedTraverse('@@event_listing')
        self.assertEqual(len(view._get_events()), 5)

    def test_get_events_all(self):
        self.request.form.update({'mode': 'all'})
        view = self.portal.restrictedTraverse('@@event_listing')
        self.assertEqual(len(view._get_events()), 8)

    def test_get_events_today(self):
        today = localized_today().isoformat()
        self.request.form.update({'mode': 'day', 'date': today})
        view = self.portal.restrictedTraverse('@@event_listing')
        self.assertEqual(len(view._get_events()), 2)

    def test_events_listing_ical(self):
        # Default mode is to show all events from now on.
        view = self.portal.restrictedTraverse('@@event_listing_ical')
        view()  # At least, this should not fail.
                # Don't know yet how to catch Content-Disposition output
        #out = view()
        #self.assertEqual(out.count('BEGIN:VEVENT'), 8)