(module

    (import "console" "log" (func $log (param i32)))

    (memory $memory 1)
    (export "memory" (memory $memory))

    ;; Current memory index, and
    ;; Size of an i32 in memory in bytes
    (global $input_index (mut i32) (i32.const 0))
    (global $size i32 (i32.const 4))

    ;; Delimiters
    (global $end_group i32 (i32.const 0))

    ;; Store largest sum seen so far
    (global $largest_sum (mut i32) (i32.const 0))

    (func $inc_index
        global.get $input_index
        global.get $size
        i32.add
        global.set $input_index
    )

    (func $loop_if_nz (result i32)
        global.get $end_group
        global.get $input_index
        i32.load
        i32.ne
    )

    (func (export "main") (result i32)
        (local $group_sum i32)

        loop
            loop 

                ;; Load current group sum
                local.get $group_sum
                
                ;; Get next calorie value
                global.get $input_index
                i32.load

                ;; Add calorie value to sum
                i32.add
                local.set $group_sum

                ;; Increment $input_index
                call $inc_index

                ;; Loop if 0 != memory[$input_index] 
                call $loop_if_nz
                br_if 0
            end

                ;; Push value for "select"
                local.get $group_sum
                global.get $largest_sum

                ;; Push values for "gt_s"
                local.get $group_sum
                global.get $largest_sum
                
                i32.gt_s  ;; $temp > $largest_sum 
                select    ;; ($temp > $largest_sum) ? $temp : $largest_sum
                
                global.set $largest_sum

                ;; Reset group sum
                i32.const 0
                local.set $group_sum

                ;; Increment $input_index 
                call $inc_index

                ;; Loop if 0 != memory[$input_index]
                call $loop_if_nz
                br_if 0
        end

        global.get $largest_sum
    )
)
