pragma solidity >=0.4.22 <0.7.0;

contract realEstate {
    enum State = {Not-Initialised, In-Process, Completeted}
    
    State state private;
    
    
    address public auth1 = '';
    string private timeEndsIn;
    //set access to authortity only
    
    constructor (_time) public {
        state = State.Not-Initialised;
        timeEndsIn = timeNow + _time;
    }
    
    function getState() {
        return state;
    }
    function verify(documents) public {
        state = State.In-Process;    
    }
    
    modifier unlesstime () {
        
    }
    
    function send(address receiver, uint amount) public [unlesstime]{
        
    }
    
    function complete() {
        state = State.Complete;
    }
    
}