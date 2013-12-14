angular.module('reddit', ['ngResource'])

.factory('SubReddit', function($resource) {
    return $resource('/api/r/sr/:subreddit/:type', {type:'new'},
        {
            get : {method:'GET', isArray: false}
        }
    );
})

.controller('SubRedditCtrl', function($scope, SubReddit){
    $scope.messages = "No data to display now.";
    $scope.datatype = 'new';
    $scope.submissions = [];

    $scope.search = function(){
        $scope.submissions = [];
        $scope.messages = "Loading...";
        SubReddit.get(
            {
                subreddit:$scope.subreddit,
                type:$scope.datatype
            },
            function(result){
                $scope.submissions = result.result;
            },        
            function(result){
                $scope.submissions = [];
                $scope.messages = result.data.error_msg;
            }
        );
    };
});