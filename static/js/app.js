var App = angular.module('App', ['ngRoute',]).controller('GlobalController', globalController);

App.config(function ($routeProvider, $locationProvider) { 
    $routeProvider
        .when('/', { 
                controller: 'IndexController',
                templateUrl: '/static/partials/index.html'
            })
        .when('/school/:id/:list', {
                controller: 'ListController',
                templateUrl: '/static/partials/list.html'
            })
        .when('/school/:id', {
                controller: 'SchoolController',
                templateUrl: '/static/partials/school.html'
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

        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
});

App.directive('fixmouse', function() { 
    element.bind('mouseenter', function(event) { 
        console.log("Entered");
    });
});

App.directive('ngEnter', function() { 
    return function(scope, element, attrs) { 
        list = new Array();
        element.bind("keyup", function(event) { 
            /* 
            // This shit isn't working right, so I'm going to leave it alone for now.
            if(event.which === 27) { // Esc key
                // $(".focused").removeClass("focused");
                list = new Array();
                scope.$apply(function() { 
                    scope.selectingSchools = false;
                    scope.selectIndex = null;
                    delete scope.selectIndex;
                });
            };
            */

            /*
            if(event.which === 13) { // Enter
                console.log("ENTER!");
            };
            */

            /*
            if(event.which === 40 || event.which === 38) { // Up or Down arrows
                // $(".focused").removeClass("focused");
                if(scope.formSubmitted) { 
                    $("div.result").children().not(".hidden").each(function(index, item) { 
                        list[index] = item;
                    });
                    scope.$apply(function() {
                        scope.selectingSchools = true;
                        if(typeof(scope.selectIndex) == 'undefined')
                            scope.selectIndex = 0;
                        else {
                            if(event.which === 40) { // Down arrow
                                // prevent from going bigger than the list.
                                if(scope.selectIndex > list.length-2) {
                                    scope.selectingSchools = false;
                                } else { 
                                    scope.selectIndex++;
                                    scope.selectingSchools = true;
                                }
                            }
                            else if(event.which === 38) { // Up arrow
                                // prevent from going smaller than zero.
                                if(scope.selectIndex <= 0) { 
                                    scope.selectingSchools = false;
                                } else { 
                                    scope.selectIndex--;
                                    scope.selectingSchools = true;
                                }
                            }
                        }
                        $(list[scope.selectIndex]).parent().addClass("focused");
                    });
                };
            };
            */

            /*
            if(event.which === 8) {  // Delete/Backspace key
                if(typeof(scope.name) == 'undefined') { 
                    // Empty shits out.
                    scope.$apply(function() { 
                        scope.schools = null;
                        scope.formSubmitted = false;
                    });
                } else if(scope.name == "") {
                    scope.$apply(function() { 
                        scope.schools = null;
                        scope.formSubmitted = false;
                    });
                } else { 
                    scope.$apply(function() { 
                        scope.submitForm();
                    });
                }
            }
            */

            if(typeof(scope.name) == 'undefined') { 
                // bail. Don't bother if name is empty.
            } else { 
                scope.$apply(function() { 
                    scope.$eval(attrs.ngEnter);
                    if(scope.name.length == 0) { 
                        scope.formSubmitted = false;
                    }
                    if(scope.name.length > 3) { 
                        scope.submitForm();
                    }
                });
            };
        });
    }
});

var controllers = {};

function globalController($scope) { 
    console.log("Global");
    $scope.formSubmitted = false;
    $scope.selectIndex = 0;
};

controllers.ListController = function($scope, $http, $routeParams) { 
    var url = "/api/schools/" + $routeParams.id + "/";
    $http({method: 'GET', url: url})
        .success(function(data, status, headers, config) {
            $scope.school = data;
            $scope.mapStyle = {
                'background'        : 'url(' + $scope.school.background + ') no-repeat',
                'background-size'   : '100% auto',
            };
        });

    var list_url    = "/api/lists/" + $routeParams.list + "/";
    $http({method: 'GET', url: list_url})
        .success(function(data, status, headers, config) { 
            $scope.list = data;
        });

    var item_url    = "/api/items/list/" + $routeParams.list + "/";
    $http({method: 'GET', url: item_url})
        .success(function(data, status, headers, config) { 
            $scope.items = data;
        });

    var checkout_url = "/api/checkout/" + $routeParams.list + "/";
    $http({method: 'GET', url: checkout_url})
        .success(function(data, status, headers, config) { 
            $scope.checkout = data;
        });

    var checkout_url = "/api/checkout/" + $routeParams.list + "/";
    
}

controllers.SchoolController = function($scope, $http, $routeParams) { 
    $scope.getListsForCategory = function(school, category) { 
        $scope.categoryTimeout = category;

        if($scope.selectedCategory == category)
            $scope.selectedCategory = null;
        else
            $scope.selectedCategory = category;

        var list_url = "/api/lists/list/" + school + "/" + category + "/";
        $http({method: 'GET', url: list_url})
            .success(function(data, status, headers, config) {
                $scope.lists_for_category = data;
                $scope.categoryTimeout = null;
            });
    }

    var url = "/api/schools/" + $routeParams.id + "/";
    $http({method: 'GET', url: url})
        .success(function(data, status, headers, config) {
            $scope.school = data;
            $scope.mapStyle = {
                'background'        : 'url(' + $scope.school.background + ') no-repeat',
                'background-size'   : '100% auto',
            };
        });

    var category_url = "/api/categories/list/" + $routeParams.id + "/";
    $http({method: 'GET', url: category_url})
        .success(function(data, status, headers, config) { 
            $scope.categories = data;
        });

    var list_url    = "/api/lists/list/" + $routeParams.id + "/";
    $http({method: 'GET', url: list_url})
        .success(function(data, status, headers, config) { 
            $scope.lists = data;
        });
}

controllers.IndexController = function($scope) { 
}

App.controller(controllers);

