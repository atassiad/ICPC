function nodeFactory(value, nextNode) {
    return {value: value, nextNode: nextNode};
}

export class LL {
    constructor(){
        this.head = nodeFactory(0, null)
    }

    append(value) {
        let newNode = nodeFactory(value, null)
        let tempNode = this.head;

        while (tempNode.nextNode != null){
            tempNode = tempNode.nextNode;
        }

        tempNode.nextNode = newNode;
    }

    prepend(value) {
        let newNode = nodeFactory(value, null)
        newNode.nextNode = this.head
        this.head = newNode
    }

    toString() {
        let tempNode = this.head;
        let return_str = "";

        while (tempNode.nextNode != null){
            return_str += "( " + tempNode.value + " )" + " -> ";
            tempNode = tempNode.nextNode;
        }

        return_str += "( " + tempNode.value + " )" + " -> ";
        return_str += "null";

        return return_str;
    }
};

