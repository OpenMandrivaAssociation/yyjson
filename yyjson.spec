Name:           yyjson
Release:        1
Version:        0.10.0
Summary:        A high performance JSON library written in ANSI C
License:        MIT
URL:            https://github.com/ibireme/yyjson
Source0:        https://github.com/ibireme/yyjson/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake

%description
A high performance JSON library written in ANSI C.

Features
- Fast: can read or write gigabytes per second JSON data on modern CPUs.
- Portable: complies with ANSI C (C89) for cross-platform compatibility.
- Strict: complies with RFC 8259 JSON standard, ensuring strict number format
and UTF-8 validation.
- Extendable: offers options to allow comments, trailing commas, NaN/Inf, and
custom memory allocator.
- Accuracy: can accurately read and write int64, uint64, and double numbers.
- Flexible: supports unlimited JSON nesting levels, \u0000 characters, and non
null-terminated strings.
- Manipulation: supports querying and modifying using JSON Pointer, JSON Patch
and JSON Merge Patch.
- Developer-Friendly: easy integration with only one h and one c file.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1

# https://github.com/ibireme/yyjson/issues/154
sed -i '/-Werror/d' CMakeLists.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DYYJSON_BUILD_TESTS=ON

%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_libdir}/libyyjson.so.0*

%files devel
%{_includedir}/yyjson.h
%{_libdir}/libyyjson.so
%{_libdir}/cmake/yyjson/
%{_libdir}/pkgconfig/yyjson.pc
