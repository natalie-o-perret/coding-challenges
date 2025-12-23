const std = @import("std");

fn countHousesWithRobo(directions: []const u8) !u32 {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var santa_x: i32 = 0;
    var santa_y: i32 = 0;
    var robo_x: i32 = 0;
    var robo_y: i32 = 0;
    var visited = std.AutoHashMap([2]i32, void).init(allocator);
    defer visited.deinit();

    try visited.put([2]i32{ 0, 0 }, {});

    for (directions, 0..) |c, i| {
        if (i % 2 == 0) { // Santa's turn
            switch (c) {
                '^' => santa_y += 1,
                'v' => santa_y -= 1,
                '>' => santa_x += 1,
                '<' => santa_x -= 1,
                else => {},
            }
            try visited.put([2]i32{ santa_x, santa_y }, {});
        } else { // Robo-Santa's turn
            switch (c) {
                '^' => robo_y += 1,
                'v' => robo_y -= 1,
                '>' => robo_x += 1,
                '<' => robo_x -= 1,
                else => {},
            }
            try visited.put([2]i32{ robo_x, robo_y }, {});
        }
    }

    return visited.count();
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();

    // Test cases with assertions
    std.debug.assert(try countHousesWithRobo("^v") == 3);
    std.debug.assert(try countHousesWithRobo("^>v<") == 3);
    std.debug.assert(try countHousesWithRobo("^v^v^v^v^v") == 11);

    const input = try std.fs.cwd().readFileAlloc(gpa.allocator(), "../input.txt", 1024 * 1024);
    defer gpa.allocator().free(input);
    const directions = std.mem.trim(u8, input, &std.ascii.whitespace);

    const result = try countHousesWithRobo(directions);
    std.debug.print("Zig: {d}\n", .{result});
}
