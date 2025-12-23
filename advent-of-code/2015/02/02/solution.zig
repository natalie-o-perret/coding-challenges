const std = @import("std");

fn calculateRibbon(dimensions: []const u8) !u32 {
    var it = std.mem.splitScalar(u8, dimensions, 'x');
    var dims_array: [3]u32 = undefined;
    var i: usize = 0;

    while (it.next()) |part| {
        const num = try std.fmt.parseInt(u32, part, 10);
        dims_array[i] = num;
        i += 1;
    }

    // Sort dimensions
    std.mem.sort(u32, &dims_array, {}, comptime std.sort.asc(u32));

    // Smallest perimeter (using two smallest dimensions)
    const perimeter = 2 * (dims_array[0] + dims_array[1]);

    // Volume for bow
    const volume = dims_array[0] * dims_array[1] * dims_array[2];

    return perimeter + volume;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();

    // Test cases with assertions
    std.debug.assert(try calculateRibbon("2x3x4") == 34);
    std.debug.assert(try calculateRibbon("1x1x10") == 14);

    const input = try std.fs.cwd().readFileAlloc(gpa.allocator(), "../input.txt", 1024 * 1024);
    defer gpa.allocator().free(input);

    var total: u32 = 0;
    var lines = std.mem.splitScalar(u8, input, '\n');
    while (lines.next()) |line| {
        if (line.len > 0) {
            total += try calculateRibbon(line);
        }
    }
    std.debug.print("Zig: {d}\n", .{total});
}
