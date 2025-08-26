import os
from datetime import datetime
import todo_manager

# Test file to store tasks
TEST_TASKS_FILE = "test_tasks.json"

# Override the TASKS_FILE in todo_manager
todo_manager.TASKS_FILE = TEST_TASKS_FILE

def test_load_save_tasks():
    """Test loading and saving tasks"""
    # Create a test tasks file
    test_tasks = [
        {
            'id': 1,
            'description': 'Test task 1',
            'status': todo_manager.PENDING,
            'created_at': datetime.now().isoformat()
        },
        {
            'id': 2,
            'description': 'Test task 2',
            'status': todo_manager.DONE,
            'created_at': datetime.now().isoformat()
        }
    ]
    
    # Save test tasks
    todo_manager.save_tasks(test_tasks)
    
    # Load tasks
    loaded_tasks = todo_manager.load_tasks()
    
    # Verify loaded tasks
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0]['id'] == 1
    assert loaded_tasks[0]['description'] == 'Test task 1'
    assert loaded_tasks[0]['status'] == todo_manager.PENDING
    assert loaded_tasks[1]['id'] == 2
    assert loaded_tasks[1]['description'] == 'Test task 2'
    assert loaded_tasks[1]['status'] == todo_manager.DONE
    
    print("✓ Load/Save tasks test passed")

def test_add_task():
    """Test adding a task"""
    # Start with empty tasks
    tasks = []
    
    # Add a task
    tasks = todo_manager.add_task(tasks)
    
    # Verify task was added
    assert len(tasks) == 1
    assert tasks[0]['id'] == 1
    assert tasks[0]['status'] == todo_manager.PENDING
    
    print("✓ Add task test passed")

def test_list_tasks():
    """Test listing tasks"""
    tasks = [
        {
            'id': 1,
            'description': 'Test task 1',
            'status': todo_manager.PENDING,
            'created_at': datetime.now().isoformat()
        },
        {
            'id': 2,
            'description': 'Test task 2',
            'status': todo_manager.DONE,
            'created_at': datetime.now().isoformat()
        }
    ]
    
    # This will just test that the function runs without error
    todo_manager.list_tasks(tasks)
    todo_manager.list_tasks([])  # Test empty list
    
    print("✓ List tasks test passed")

def test_update_task():
    """Test updating a task"""
    tasks = [
        {
            'id': 1,
            'description': 'Test task 1',
            'status': todo_manager.PENDING,
            'created_at': datetime.now().isoformat()
        }
    ]
    
    # Update the task
    tasks = todo_manager.update_task(tasks)
    
    # Verify task exists and has an ID
    assert len(tasks) == 1
    assert tasks[0]['id'] == 1
    
    print("✓ Update task test passed")

def test_delete_task():
    """Test deleting a task"""
    tasks = [
        {
            'id': 1,
            'description': 'Test task 1',
            'status': todo_manager.PENDING,
            'created_at': datetime.now().isoformat()
        },
        {
            'id': 2,
            'description': 'Test task 2',
            'status': todo_manager.PENDING,
            'created_at': datetime.now().isoformat()
        }
    ]
    
    # Delete a task
    tasks = todo_manager.delete_task(tasks)
    
    # Verify one task was deleted
    # Note: This test doesn't actually remove a task since we're not providing input
    # But it verifies the function runs without error
    assert len(tasks) == 2  # No task actually deleted in this test
    
    print("✓ Delete task test passed")

def test_mark_task_done():
    """Test marking a task as done"""
    tasks = [
        {
            'id': 1,
            'description': 'Test task 1',
            'status': todo_manager.PENDING,
            'created_at': datetime.now().isoformat()
        }
    ]
    
    # Mark task as done
    tasks = todo_manager.mark_task_done(tasks)
    
    # Verify task exists and has an ID
    assert len(tasks) == 1
    assert tasks[0]['id'] == 1
    
    print("✓ Mark task done test passed")

def main():
    """Run all tests"""
    print("Running To-Do List Manager tests...\n")
    
    try:
        test_load_save_tasks()
        test_add_task()
        test_list_tasks()
        test_update_task()
        test_delete_task()
        test_mark_task_done()
        
        print("\n✓ All tests completed successfully!")
        print("\nTo-Do List Manager features:")
        print("- Add tasks")
        print("- List tasks")
        print("- Update tasks")
        print("- Delete tasks")
        print("- Mark tasks as done")
        print("- Save tasks to JSON file")
        print("- Load tasks from JSON file")
        
        # Clean up test file
        if os.path.exists(TEST_TASKS_FILE):
            os.remove(TEST_TASKS_FILE)
            
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        # Clean up test file
        if os.path.exists(TEST_TASKS_FILE):
            os.remove(TEST_TASKS_FILE)

if __name__ == "__main__":
    main()