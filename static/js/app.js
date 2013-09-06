var App = angular.module('App', ['restangular']).controller('GlobalController', globalController);

App.config(function ($routeProvider) { 
    $routeProvider
        .when('/', 
            { 
                controller: 'IndexController',
                templateUrl: '/static/js/partials/index.html'
            })
        .when('/about', 
            {
                templateUrl: '/static/js/partials/about.html'
            })
        .when('/about/directors', 
            {
                controller: 'DirectorController',
                templateUrl: '/static/js/partials/directors.html'
            })
        .when('/about/officers', 
            {
                controller: 'OfficerController',
                templateUrl: '/static/js/partials/officers.html'
            })
        .when('/about/faq', 
            {
                templateUrl: '/static/js/partials/faq.html'
            })
        .when('/resources',
            {
                controller: 'ResourcesController',
                templateUrl: '/static/js/partials/resources.html'
            })
        .when('/news',
            {
                controller: 'NewsController',
                templateUrl: '/static/js/partials/news.html'
            })
        .when('/search',
            {
                controller: 'SearchController',
                templateUrl: 'search.html'
            })
        .otherwise({ redirectTo: '/' });
});

App.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('/api/v1');
    RestangularProvider.setRequestSuffix('');
    RestangularProvider.setResponseExtractor(function(response, operation, what, url) {
        var newResponse;
        if (operation === "getList") {
            newResponse = response.objects;
            newResponse.metadata = response.meta;
        } else {
            newResponse = response.data;
        }
        return newResponse;
    });
});

App.directive('ngEnter', function() { 
    return function(scope, element, attrs) { 
        element.bind("keyup", function(event) { 
            scope.$apply(function() { 
                scope.$eval(attrs.ngEnter);
                if(scope.name.length > 3) { 
                    scope.submitForm();
                }
            });
        });
    }
});

var controllers = {};

function globalController($scope) { 
    $scope.greeting = 'Hola';
    console.log("Global");
};

controllers.IndexController = function($scope, Restangular) { 
    $scope.submitForm = function() { 
        Restangular.all('schools/search/?q=' + $scope.name, {'q': $scope.name}).getList().then(function(schools) { 
            $scope.schools = schools;
            console.log(schools);
        });
        /*
        $.get('/api/v1/schools/search/?q=north', function(data) { 
            console.log(data);
        });
        */
        console.log("YAY");
    };
    /*
    Restangular.all('schools').getList().then(function(schools) { 
        $scope.schools = schools;
    });
    */
}

controllers.ResourcesController = function ($scope, Restangular) { 
    Restangular.all('study').getList().then(function(resources) { 
        $scope.resources = resources;
    });
}

controllers.DirectorController = function ($scope, Restangular) { 
    Restangular.all('directors').getList().then(function(directors) { 
        $scope.directors = directors;
    });
}

controllers.OfficerController = function($scope, Restangular) { 
    Restangular.all('officers').getList().then(function(officers) { 
        $scope.officers = officers;
    });
}

controllers.NewsController = function($scope, Restangular) { 
    Restangular.all('news').getList().then(function(news) { 
        $scope.news = news;
    });
}

App.controller(controllers);

