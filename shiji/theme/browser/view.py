from Products.Five import BrowserView
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from plone.app.contenttypes.interfaces import INewsItem
from plone.app.contenttypes.interfaces import IEvent
from plone.app.contenttypes.interfaces import IFile
from shiji.content.proposal import IProposal


class FrontPage(BrowserView):

    def Title(self):
        portal_state = getMultiAdapter((self.context, self.request), name='plone_portal_state')
        portal = portal_state.portal()
        fp = portal.restrictedTraverse('front-page', default=None)
        if fp:
            return fp.Title()
        else:
            return None

    def get_news(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/news'
        query = {}
        query['object_provides'] = INewsItem.__identifier__
        query['path'] = path
        query['state'] = ('published', )
        query['sort_on'] = 'created'
        query['sort_order'] = 'reverse'
        limit = 3
        result = []
        brains = catalog(**query)[:limit]
        for b in brains:
            sdate = str(b.created)[:10].replace('/','-')
            result.append((b.Title, sdate, b.getURL()))
        return result

    def get_event(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/events'
        query = {}
        query['object_provides'] = IEvent.__identifier__
        query['path'] = path
        query['state'] = ('published', )
        query['sort_on'] = 'start'
        query['sort_order'] = 'reverse'
        limit = 3
        result = []
        brains = catalog(**query)[:limit]
        for b in brains:
            sdate = str(b.start)[:10].replace('/','-')
            result.append((b.Title, sdate, b.getURL()))
        return result

    def get_info(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/bulletin'
        query = {}
        query['object_provides'] = IFile.__identifier__
        query['path'] = path
        query['state'] = ('published', )
        query['sort_on'] = 'created'
        query['sort_order'] = 'reverse'
        limit = 3
        result = []
        brains = catalog(**query)[:limit]
        for b in brains:
            sdate = str(b.created)[:10].replace('/','-')
            result.append((b.Title, sdate, b.getURL()))
        return result

    def get_issue(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/issue'
        query = {}
        query['object_provides'] = IProposal.__identifier__
        query['path'] = path
        query['state'] = ('private', )
        query['sort_on'] = 'created'
        query['sort_order'] = 'reverse'
        limit = 3
        result = []
        brains = catalog(**query)[:limit]
        for b in brains:
            sdate = str(b.created)[:10].replace('/','-')
            result.append((b.Title, sdate, b.getURL()))
        return result

    def get_minutes(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')
        path = portal_state.navigation_root_path() + '/minutes'
        query = {}
        query['object_provides'] = IFile.__identifier__
        query['path'] = path
        query['state'] = ('private', )
        query['sort_on'] = 'created'
        query['sort_order'] = 'reverse'
        limit = 3
        result = []
        brains = catalog(**query)[:limit]
        for b in brains:
            sdate = str(b.created)[:10].replace('/','-')
            result.append((b.Title, sdate, b.getURL()))
        return result

