use hello::{add, greeting};

#[test]
#[allow(non_snake_case)]
fn BasicAddition() {
    assert_eq!(add(2, 3), 5);
    assert_eq!(add(-1, 1), 0);
    assert_eq!(add(0, 0), 0);
}

#[test]
fn greeting_is_hello_world() {
    assert_eq!(greeting(), "Hello, World!");
<<<<<<< HEAD
}
=======
}
>>>>>>> origin/develop
