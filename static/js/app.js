App = Ember.Application.create();

App.Router.map(function() {
    this.resource('news');
    this.resource('resources');
    this.resource('about', {path: '/about'}, function() {
        this.route('faq');
        this.resource('directors');
        this.resource('officers');
    });
});

App.AboutRoute = Ember.Route.extend({ });

App.NewsRoute = Ember.Route.extend({ 
    model: function() { 
        return $.getJSON('/api/v1/news/?format=json').then(function(data) {
            return data.objects;
        });
    }
});

App.ResourcesRoute = Ember.Route.extend({ 
    model: function() { 
        return $.getJSON('/api/v1/study/?format=json').then(function(data) {
            return data.objects;
        });
    }
});

App.OfficersRoute = Ember.Route.extend({ 
    model: function() { 
        return $.getJSON('/api/v1/officers/?format=json').then(function(data) {
            return data.objects;
        });
    }
});

App.DirectorsRoute = Ember.Route.extend({ 
    model: function() { 
        return $.getJSON('/api/v1/directors/?format=json').then(function(data) {
            return data.objects;
        });
    }
});

App.IndexRoute = Ember.Route.extend({
});

var directors = [{
    id:     '1',
    name:   'James Scobey',
    title:  'Director'
}, {
    id:     '2',
    name:   'Barry Melton',
    title:  'Director'
}, {
    id:     '3',
    name:   'Derrick Tittsworth',
    title:  'Director'
}]

var officers = [{
    id:     '1',
    name:   'Misty Melton',
    title:  'President'
}, {
    id:     '2',
    name:   'Stephanie Boudreaux',
    title:  'Treasurer / Secretary'
}]

/*
var resources = [{
    id:     '1',
    title:  'Teaching Salary: The Secret Cost of Teaching',
    url:    'http://www.scholastic.com/teachers/article/teaching-salary-secret-cost-teaching',
    source: 'Scholastic',
    source_url: 'http://scholastic.com',
    date:   '2010',
}, {
    id:     '2',
    title:  'Teachers Spend $1.3 Billion Out of Pocket on Classroom Materials',
    url:    'http://thejournal.com/articles/2010/07/08/teachers-spend-1.3-billion-out-of-pocket-on-classroom-materials.aspx',
    source: 'The Journal',
    source_url: 'http://thejournal.com',
    date    : '2010',
}]
*/

App.store = DS.Store.create({
    adapter: DS.DjangoTastypieAdapter.extend({
        serverDomain: "http://supportclassrooms.com",
        namespace: "api/study"
    })
})

var resources = DS.Model.extend({ 

});

var showdown = new Showdown.converter();
Ember.Handlebars.registerBoundHelper('markdown', function(input) {
    return new Ember.Handlebars.SafeString(showdown.makeHtml(input));
});
