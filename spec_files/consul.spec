%undefine _disable_source_fetch
%define debug_package %{nil}
Name:           consul
Version:        jeff
Release:        1.2.3
Summary:        consul service discovery

Group:          nomad_cloud
BuildArch:      x86_64
License:        MPL2
URL:            https://www.consul.io/
Source0:        https://releases.hashicorp.com/consul/1.2.3/consul_1.2.3_linux_amd64.zip
Source1:        https://github.com/jeffreyhodge/cloud/raw/master/systemd/consul.service

%description
Service registry and kv store

%prep
%setup -q -c -n builddir
%build
%install
cp %{_sourcedir}/consul.service %{_builddir}/builddir
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/sbin
install -m 0755 consul $RPM_BUILD_ROOT/usr/local/sbin/consul
install -m 0755 -d $RPM_BUILD_ROOT/etc/consul.d
install -m 0755 -d $RPM_BUILD_ROOT/etc/systemd/system
install -m 0644 consul.service $RPM_BUILD_ROOT/etc/systemd/system/consul.service

%files
/usr/local/sbin/consul
/etc/consul.d
/etc/systemd/system/consul.service

%pre
getent group consul >/dev/null || groupadd -r consul
getent passwd consul >/dev/null || \
    useradd -r -g consul -d /home/consul -s /sbin/nologin \
    -c "Consul user" consul
exit 0

%changelog
