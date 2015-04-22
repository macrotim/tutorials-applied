function Ctrl($scope) {
    $scope.data = {message: "Hello"};
}

function FirstCtrl($scope) {
}

var myApp = angular.module('myApp', []);
myApp.factory('DataA', function() {
    return {message: "I'm data from a service"}
})
myApp.factory('DataB', function() {
    return {message: "health goth post-ironic"}
})

function FirstAppCtrl($scope, DataA) {
    $scope.data = DataA;
}

function SecondAppCtrl($scope, DataA) {
    $scope.data = DataA;
}

function MethodCtrl1($scope, DataB) {
    $scope.data = DataB;
}

function MethodCtrl2($scope, DataB) {
    $scope.data = DataB;

    $scope.reversed = function(msg) {
        return msg.split("").reverse().join("");
    };
}
